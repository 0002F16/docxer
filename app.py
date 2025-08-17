# app.py
import streamlit as st
from pathlib import Path
import tempfile
import subprocess
import sys

st.set_page_config(page_title="DOCX Proofreader", layout="centered")
st.title("📝 DOCX Proofreader")

SCRIPT_PATH = Path(__file__).resolve().parent / "proofreader.py"
SCRIPT_DIR = SCRIPT_PATH.parent

if not SCRIPT_PATH.exists():
    st.error(f"Could not find proofreader at: {SCRIPT_PATH}")
    st.stop()

st.caption(f"Using script: `{SCRIPT_PATH}`")

uploaded = st.file_uploader("Upload a .docx file", type=["docx"])
use_public_api = st.toggle("Use public LanguageTool API (no Java required)", value=True)
run_btn = st.button("Run Proofreader", type="primary", disabled=uploaded is None)

if run_btn and uploaded:
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        input_doc = td / uploaded.name
        output_doc = td / (input_doc.stem + "_corrected" + input_doc.suffix)
        input_doc.write_bytes(uploaded.getbuffer())

        # Build command
        cmd = [
            sys.executable,           # current interpreter
            str(SCRIPT_PATH),
            "-i", str(input_doc),
            "-o", str(output_doc),
        ]
        if use_public_api:
            cmd.append("--remote")

        st.info("Running proofreader… This may take a moment on large documents.")
        with st.spinner("Proofreading in progress"):
            proc = subprocess.run(
                cmd,
                cwd=str(SCRIPT_DIR),  # important so script writes logs where it expects
                capture_output=True,
                text=True
            )

        # Show raw stdout/stderr (collapsible)
        with st.expander("Show run output (stdout/stderr)"):
            st.code((proc.stdout or "") + "\n" + (proc.stderr or ""), language="bash")

        # Locate logs written by proofreader.py (it writes to its own folder)
        grammar_log = SCRIPT_DIR / "grammar_edits.log"
        skipped_log = SCRIPT_DIR / "skipped_items.log"
        no_issues_log = SCRIPT_DIR / "no_issues.log"

        # Read logs safely
        def read_log(p: Path) -> str:
            try:
                return p.read_text(encoding="utf-8")
            except Exception:
                return "(no content)"

        # Results area
        if output_doc.exists():
            st.success("Proofreading complete!")
            st.download_button(
                "⬇️ Download corrected DOCX",
                data=output_doc.read_bytes(),
                file_name=output_doc.name,
                type="primary"
            )
        else:
            st.error("No output file was produced. Check the run output above for errors.")

        st.subheader("Logs")
        tabs = st.tabs(["Grammar Edits", "Skipped Items", "No Issues"])
        with tabs[0]:
            st.text_area(
                "grammar_edits.log",
                read_log(grammar_log),
                height=300
            )
            st.download_button("Download grammar_edits.log", data=read_log(grammar_log), file_name="grammar_edits.log")
        with tabs[1]:
            st.text_area(
                "skipped_items.log",
                read_log(skipped_log),
                height=300
            )
            st.download_button("Download skipped_items.log", data=read_log(skipped_log), file_name="skipped_items.log")
        with tabs[2]:
            st.text_area(
                "no_issues.log",
                read_log(no_issues_log),
                height=300
            )
            st.download_button("Download no_issues.log", data=read_log(no_issues_log), file_name="no_issues.log")
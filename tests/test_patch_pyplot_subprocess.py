from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def test_patch_pyplot_merges_defaults_in_fresh_interpreter(tmp_path: Path) -> None:
    """Avoid mutating ``plt.savefig`` in the pytest process."""
    repo = Path(__file__).resolve().parents[1]
    out = tmp_path / "patched.png"
    code = f"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import signalplot as sp

sp.apply()
sp.patch_pyplot()
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
plt.savefig({str(out)!r})
plt.close(fig)
"""
    env = {**os.environ, "PYTHONPATH": str(repo)}
    proc = subprocess.run(
        [sys.executable, "-c", code],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout
    assert out.is_file()
    assert out.stat().st_size > 0

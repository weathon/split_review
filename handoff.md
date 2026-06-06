Understand current repo, mainly `code/main.py` first. Then do:
Add one new scripts to `code/` that re-score from a cached merger pipeline log, similar to `notebooks/post_hoc.ipynb` (only the part about extracting cache is valid, ignore other parts, that means without calibration (output raw scores directly).)

Follow the structure of `code/rebuttal.py` or `code/main.py` (multi-SDK support). Each script should have a matching bash launcher in `scripts/`, modeled on the rebuttal bash, that takes the merger log path and other parameters as inputs.

Outputs a single review with a score and accept/reject decision and 6 subscores. Directly from the cached pipeline. This should be the same as using merger.md prompt with cal_without.md, with 2 differences:
1. instead of re-run, it use cached thing from the log. 
2. Instead of single score and decision, it outputs 6 other sub scores. Each subscore ranges 0–5, and the sub score dims are: Originality, Importance of the research question, Whether claims are well supported, Soundness of experiments, Clarity of writing, Value to the research community. 
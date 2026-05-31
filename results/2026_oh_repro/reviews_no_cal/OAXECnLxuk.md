## Summary
This paper introduces **DaVinci**, a two-stage training pipeline for **diagram image → TikZ code** parsing: (i) SFT on a newly curated **TikZ30K** dataset (with code reordering and comment annotations), followed by (ii) GRPO-based RL using a **hybrid reward** intended to encourage compilability, visual fidelity, and text/geometry alignment. Experiments on the DATiKZ\_v3 test set show strong gains in compile rate and image-level similarity metrics, with additional human evaluation comparing DaVinci to selected open and proprietary MLLMs.

## Strengths
- **Clear, concrete dataset contribution with measured impact.** The paper isolates the effect of **code reordering** and **comment injection** on SFT compile success: Pass@1 rises from **69.74 → 78.78 → 84.50** as these dataset features are added (Table 4; lines 240–255), and the paper quantifies the deltas (+9.04%, +5.72%; line 246).
- **Strong end-task compilation performance and broad automatic evaluation.** On DATiKZ\_v3, DaVinci-7B achieves **97.60 Pass@1** (Table 1; line 190) and reports multiple code- and image-level metrics (Pass@1, TED, cBLEU; DreamSim/SigLIP/SSIM/MSE/LPIPS) with explicit definitions (lines 168–169).
- **Human evaluation is present and methodologically specified.** The Best–Worst Scaling setup is described (100 items, 6 evaluators, scoring procedure, SHR reliability) and results are given for two comparison groups (lines 214–236).

## Weaknesses

### Fatal
None.

### Major
- **Headline claim “surpasses… GPT-5 and Claude” is not supported by the paper’s own human-eval results as stated.** The abstract claims DaVinci “surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4” (line 9). However, in the proprietary human-eval group (Table 3), **DaVinci-7B has score −0.01**, while **GPT-5-Default is −0.13** and **Claude-Sonnet-4-Thinking is −0.35**, and **Gemini-2.5-Pro-Thinking is +0.50** (lines 229–235). This does support “better than GPT-5/Claude” *within that particular table*, but it does **not** support the broader framing of “surpasses leading proprietary models” in general because (i) the same table shows a proprietary model (Gemini) substantially ahead of DaVinci, and (ii) the paper’s own analysis text also notes Gemini’s superior performance on several metrics (lines 194–205). The claim needs tighter conditioning (which models/which metrics/which setting) to avoid overstatement.
- **Central “diagram parsing / structural” framing is only weakly validated by the reported metrics, which are dominated by compilation and render-similarity proxies.** The evaluation emphasizes Pass@1, text edit distance / cBLEU, and image similarity (DreamSim/SigLIP/SSIM/MSE/LPIPS) (lines 168–169; Table 1). The RL reward ablation is also reported entirely in terms of those same image/text/geometry alignment metrics (Table 5; lines 257–268). While these are meaningful for *rendering fidelity and syntactic validity*, the paper’s framing (“reinforcing … structural relationships,” line 9; “visual-structural syntax,” title/abstract) is not directly tested with a structure-grounded metric (e.g., node-edge topology for flowcharts, object identity consistency, or AST/graph equivalence classes). As written, the evidence most strongly supports “better compilable renderings” rather than “more correct recovered structure.”

### Minor
- **RL’s incremental benefit is not cleanly demonstrated on the same human-eval axis used for headline comparisons.** The paper reports SFT vs RL differences mainly through automatic metrics (Table 1 shows DaVinci-SFT-7B vs DaVinci-7B; line 189–190) and a reward-component ablation conducted “based on DaVinci-SFT-7B” (lines 257–268). But the human evaluation compares **DaVinci-7B** against other models (Tables 2–3) without an SFT-only entry in the same human-eval setting, making it harder to attribute the human-perceived gains specifically to RL rather than to the dataset/SFT stage.

### Trivial
None.

## Nice-to-Haves
- Add at least one **structure-sensitive evaluation** aligned with the paper’s “structural relationships” claim (e.g., extract graph structure from TikZ for flowcharts and report node/edge F1; measure text-to-node attachment accuracy; or compare canonicalized TikZ AST components). This would also make the RL objective’s “structure” contribution more falsifiable than render-similarity improvements alone.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“Pass@1 is a weak proxy” as a standalone criticism.** While true in general, the paper does not claim Pass@1 alone proves structural correctness; it explicitly uses multiple metrics (lines 168–169) and even states that “visually equivalent outputs can be produced by syntactically diverse TikZ code” (lines 210–211). The valid retained concern is narrower: the paper’s *structural* claim lacks a *structural* evaluation axis.
- **Speculation about unfair proprietary-model comparison protocols (prompting/tool use/budgets).** The paper states it conducts “controlled experiments” (line 156) but the excerpted text here does not provide full protocol details; without explicit on-page evidence of an asymmetry, this remains speculative.

## Novel Insights
The paper’s strongest, most defensible contribution appears to be **data/representation engineering for TikZ**—specifically, that enforcing a more canonical drawing order and adding inline code comments materially improves compilation success and downstream performance (Table 4). In contrast, the paper’s current evidence base makes the RL stage look more like **optimization of render-aligned proxies** than a clearly demonstrated improvement in *structural parsing*, suggesting the paper would land more convincingly if it reframed around “high-fidelity compilable diagram-to-TikZ generation” or added explicit structure-based tests.

## Suggestions
- Calibrate claims in the abstract/introduction to match the evidence: e.g., “outperforms GPT-5 and Claude on our protocol, but trails Gemini on human preference and several similarity metrics,” consistent with Table 3 (lines 229–235) and the analysis acknowledging Gemini’s strengths (lines 194–205).
- Add a structure-grounded metric (even on a subset) and report **SFT vs SFT+RL** on that axis; otherwise, the “reinforcing structural relationships” claim remains under-validated relative to the paper’s stated goal.

## Score and Decision
**Originality:** Moderate (combining TikZ-specific dataset curation with RL reward shaping is a reasonable extension, but the dataset engineering is the standout).  
**Importance:** High potential (diagram → editable code is valuable).  
**Claim support:** Mixed; compile/render improvements are well supported, but “structural parsing” and the broad proprietary-superiority framing are not as cleanly supported.  
**Experimental soundness:** Generally solid for the chosen proxies (automatic + human eval), but missing a structure-native validation for the central framing.  
**Clarity:** Mostly clear in experiments/ablations shown.  
**Community value:** Dataset + strong compile-rate results are useful; the RL/structure narrative needs stronger alignment.

MY FINAL SCORE: <score>6.0</score>  
MY FINAL DECISION: <decision>Reject</decision>
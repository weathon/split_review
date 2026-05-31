## Summary
DaVinci is a multimodal LLM for parsing raster scientific diagrams into structured TiKZ code, trained via a two-stage framework: supervised fine-tuning on TiKZ-30K (a newly curated dataset of 30K diagram-TiKZ pairs featuring normalized drawing order and comment annotations) followed by GRPO-based reinforcement learning guided by a hybrid reward that leverages vectorized PDF representations for extraction-error-free spatio-textual and geometric feedback. Evaluated on DATiKZ_v3, DaVinci-7B achieves a 97.60% compile rate and strong image fidelity, outperforming most proprietary MLLMs including GPT-5 and Claude-Sonnet-4 on several metrics.

---

## Strengths

- **Novel and impactful data insight**: The observation that TiKZ's rendering-order independence creates detrimental training noise is a genuinely original contribution. The ablation in Table 4 cleanly quantifies the effect: code reordering alone yields +9.04% compile rate, and comment injection adds +5.72% on top — a strong empirical validation.

- **Well-designed vectorized-representation reward**: Extracting text and geometric primitives from compiled PDFs using PyMuPDF rather than OCR is a principled and practically important insight. OCR failures on diagram symbols are a known pain point; the paper demonstrates this in Appendix E.4 and the two-step exact-then-vague matching strategy (Algorithm 1) is carefully designed. Table 5 shows progressive, consistent gains when adding Rtext and Rgeom to the baseline image reward.

- **Impressive compile-rate improvement**: DaVinci-7B achieves 97.60% Pass@1, versus ≤87% for the next-best model (Claude-Sonnet-4-Thinking at 86.90%). For practical diagram-parsing workflows, compilability is a hard constraint, making this gap highly meaningful.

- **Comprehensive evaluation**: The paper combines eight automatic metrics, two groups of human evaluation (BWS with split-half reliability ρ ≥ 0.72), detailed ablations on both data curation and reward components, and qualitative case studies — a well-rounded evidence package.

- **Responsible data handling**: The license-compliant release strategy (diff files + scripts for arXiv-licensed snippets, direct release for permissively licensed ones) is thoughtfully executed and clearly documented.

---

## Weaknesses

### Fatal
None identified.

### Major

- **Misleading abstract claim**: The abstract states DaVinci "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4." However, Table 1 shows Gemini-2.5-Pro-Thinking outperforms DaVinci-7B on DreamSim (88.20 vs. 84.83), SigLIP (95.59 vs. 93.93), SSIM (75.86 vs. 73.65), and LPIPS (21.64 vs. 22.32). More critically, Table 3 (human evaluation) shows Gemini-2.5-Pro-Thinking has a BWS score of +0.50 vs. DaVinci-7B's −0.01, a substantial gap. Gemini-2.5-Pro is unambiguously a leading proprietary model, and the paper's own results clearly establish it as a superior system for this task by all available human judgments. The abstract should not omit this finding; as written it gives a misleading picture of DaVinci's place in the landscape.

- **Conflated metrics across different semantic dimensions**: The claim of "surpassing GPT-5 and Claude-Sonnet-4" is primarily driven by compile rate and MSE. On TED, GPT-5-Default is the best open/proprietary model (53.17), beating DaVinci-7B (55.13). On DreamSim and LPIPS, DaVinci-7B slightly leads GPT-5 and Claude-Sonnet-4 but clearly trails Gemini-2.5-Pro. A more nuanced characterization of where DaVinci leads vs. trails would strengthen the paper considerably.

### Minor

- **Missing granular ablation on RL training steps/data scale**: The RL stage uses 28K samples and runs for 500 steps on 8×H100s. There is no analysis of training curves or sensitivity to the number of RL steps, rollouts (G=10 is used without justification), or data scale. This would help future practitioners replicate the benefit.

- **cBLEU regression after RL is under-analyzed**: DaVinci-7B's cBLEU drops from 7.52 (SFT) to 6.57 (RL). The paper correctly observes that high code similarity is not necessary, but does not investigate whether the RL-generated code is semantically richer or just more diverse in surface form. For practitioners relying on code-level evaluation, this matters.

- **Reordering quality not systematically measured**: Code reordering by Qwen3-Coder-480B is validated only by checking rendering consistency (before/after), but there is no measure of how many samples failed reordering, how often the model deviates from the prescribed ordering protocol, or whether reordering quality varies across diagram types (e.g., flowcharts vs. sequence diagrams vs. plots).

- **Small human evaluation sample**: 100 items out of 542 in the test set is a thin sample for human evaluation, particularly for Group 2 (DaVinci vs. proprietary models) where the score standard deviations are relatively high (e.g., Gemini-2.5-Pro std = 0.10).

### Trivial
- "LIPIIS" in line 204 appears to be a typo for "LPIPS."

---

## Nice-to-Haves

- A per-category breakdown of performance (e.g., flowcharts vs. graphs vs. neural-network diagrams) would clarify where DaVinci succeeds and where it still struggles.
- An analysis of failure cases from the 2.4% non-compiling outputs would be informative — the scatter-plot hypothesis is mentioned but not quantified.
- The "To Think or Not to Think" observation (inline comments vs. explicit chains of thought) is interesting; even a small pilot study (e.g., forcing DaVinci-7B into a thinking mode) would strengthen this claim beyond comparison with external baselines.

---

## Novel Insights

The most genuinely novel insight in the paper is the characterization of *drawing-order noise* as a first-class training problem for autoregressive TiKZ generation: unlike general programming languages, TiKZ's rendering is largely order-independent, causing the same visual output to be representable by arbitrary code permutations, which confuses sequence models trained to predict consistent orderings. The complementary insight — using compiled PDF vectorization (rather than OCR or pixel comparisons) to extract geometric and textual primitives for reward construction — is also novel in the RL-for-code-generation literature. Together, these two ideas address root causes rather than symptoms of why existing MLLMs underperform on structured diagram generation, and they are portable to other drawing languages (SVG, Mermaid) with similar properties.

---

## Suggestions

- Revise the abstract to accurately acknowledge Gemini-2.5-Pro's superiority in human evaluation and on key image-fidelity metrics. Framing DaVinci as the best open-source 7B model and competitive with (but not uniformly superior to) all proprietary systems is both accurate and compelling.
- Report training curves for RL (e.g., compile rate and DreamSim vs. step) to demonstrate stability and inform hyperparameter choices.
- Include a per-category performance breakdown to better understand generalization.
- Provide the reordering success/failure rate and examples of difficult-to-reorder diagrams to help readers assess TiKZ-30K's overall quality.

---

## Score and Decision

DaVinci presents a technically solid, well-motivated contribution to scientific diagram-to-code generation. The drawing-order normalization and vectorized-representation rewards are genuinely novel and empirically well-supported, the compile-rate result is practically impressive, and the evaluation is thorough. The primary weakness — an overstatement in the abstract about surpassing all leading proprietary models, contradicted by the paper's own human evaluation where Gemini-2.5-Pro clearly wins — is a presentation problem rather than a methodological one. The core results stand up to scrutiny and the dataset and model are planned for public release.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
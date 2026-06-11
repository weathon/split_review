Now I have a comprehensive calibration picture. Let me finalize the review.

## Summary
This paper introduces In-Context Watermarking (ICW), a method for embedding detectable watermarks in LLM-generated text purely through prompt engineering, without requiring access to the model's decoding process or weights. Four strategies at different granularities (Unicode, Initials, Lexical, Acrostics) are evaluated in both a Direct Text Stamp (DTS) and an Indirect Prompt Injection (IPI) setting, with the latter applied to detecting AI-generated peer reviews by covertly embedding watermarking instructions into academic manuscripts. Experiments on GPT-4o-mini and GPT-o3-mini demonstrate that ICW achieves near-perfect detection (ROC-AUC ≥ 0.995) with sufficiently capable models.

## Strengths
- **Novel and practically motivated problem formulation**: ICW fills a genuine gap in the watermarking literature — all prior in-process methods (Kirchenbauer et al., 2023; Aaronson, 2023) require privileged access to model logits or decoding. The paper's framing around the peer review use case (conference organizers embedding hidden instructions in manuscripts via white text, Section 3.2, Figure 2) is compelling and addresses a real, urgent need.
- **Strong detection performance with capable LLMs**: Table 2 shows all four ICW methods achieve ROC-AUC ≥ 0.995 in DTS and ≥ 0.997 in IPI with GPT-o3-mini, demonstrating that watermarking instructions embedded within long academic papers can still be reliably followed.
- **Good robustness to paraphrasing attacks**: Figure 3 shows Lexical ICW (AUC=0.924) and Acrostics ICW (AUC=0.922) substantially outperform YCZ+23 (AUC=0.557) and PostMark (AUC=0.841) under LLM paraphrasing, the most realistic adversarial modification a dishonest reviewer might employ.
- **Clear capability-dependent scaling**: The dramatic performance gap between GPT-4o-mini and GPT-o3-mini (e.g., Initials ICW ROC-AUC jumps from 0.572 to 0.999 in DTS, Table 2) directly validates the forward-looking thesis that ICW will become more viable as LLMs advance.
- **Fair and transparent baseline comparison**: The paper honestly acknowledges that PostMark and YCZ+23 are inapplicable in the IPI setting (Section 5.1, Table 2) and compares them only in DTS, avoiding misleading cross-setting comparisons.

## Weaknesses

### Fatal
None

### Major
- **IPI formulation has apparent double-counting of the instruction** (lines 91–93): The stamped text is defined as $\tilde{t} = t \oplus \text{Instruction}(\mathbf{k}, \tau)$, then the response is $y \leftarrow \mathcal{M}(\tilde{t} \oplus \text{Instruction}(\mathbf{k}, \tau) \oplus Q)$. Substituting, the instruction appears twice in the prompt. This is either an error in the equation or a discrepancy between the text (which says the instruction is embedded in $\tilde{t}$ alone) and the formula (which concatenates it again). This affects reproducibility and should be clarified.

- **Limited model diversity — only two models from a single provider**: The experiments test only GPT-4o-mini and GPT-o3-mini, both from OpenAI (Section 5.1). The central claim that ICW effectiveness scales with LLM capability is validated only within one provider's instruction-tuning paradigm. Different providers (Claude, Gemini, Llama) have different instruction-following behaviors, leaving open the possibility that ICW is an artifact of OpenAI's specific alignment approach rather than a general property of capable LLMs. Even one additional model would substantially strengthen the capability-scaling claim.

- **Text quality evaluation uses an LLM judge with systematic bias**: Table 3 shows unwatermarked GPT-o3-mini text scores 4.992 overall while human text scores 4.235 — the judge systematically rates LLM-generated text higher than human text. This well-known LLM self-preference bias means the claim that "ICW methods exhibit text quality comparable to human and unwatermarked text" (Section 5.2.3) is not well-supported: the judge may assign high scores to all LLM-generated text regardless of watermarking. The PostMark score of 2.997 may partly reflect its more aggressive text transformation rather than a meaningful quality difference.

### Minor
- **No characterization of per-sample compliance rates**: Table 2 reports only aggregate ROC-AUC, which masks whether the LLM follows the watermarking instruction consistently across outputs or only on a subset with strong watermark effect. Reporting the fraction of outputs where the z-statistic exceeds some threshold would directly address deployer reliability concerns.

- **Table 1 provides limited discriminative information**: Three of four methods (Initials, Lexical, Acrostics) receive identical filled-circle ratings on all four criteria (lines 111–116), making the summary table uninformative about trade-offs. The textual Discussion subsections are more helpful.

- **Initial letter distribution assumed from Canterbury Corpus may not generalize** (line 146): The null hypothesis for Initials ICW assumes initial-letter frequencies from the Canterbury Corpus. In practice, word-initial distributions are domain-dependent (e.g., scientific text vs. casual text), which could affect false alarm rates in the IPI experiments using ICLR papers.

### Trivial
None

## Nice-to-Haves
- A curve over perturbation rates (rather than a single 30% deletion/replacement operating point) would provide more insight into robustness trade-offs.
- Bootstrap confidence intervals on ROC-AUC would help assess reliability given n=500 samples.
- A basic evaluation of how easy it is for reviewers to detect and remove hidden IPI instructions would strengthen the motivating use case.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "No analysis of instruction detectability/removability in IPI" — the paper explicitly defers attack/defense investigation to future work (line 101), so this is scope creep rather than a missing element.
- "No discussion of model acknowledgment of hidden instructions" — too speculative; no evidence in the paper that this occurred during experiments.
- "Abstract overclaims scalability and accessibility" — the abstract says "promising direction," which is appropriately hedged for a feasibility study.
- All formatting/style nitpicks — parser artifacts, not paper problems.

## Novel Insights
The most genuinely novel observation from the reviews is the identification of the IPI equation double-counting (line 93), which appears to be either an error or a significant ambiguity in the formalization of the IPI mechanism. Beyond this, the reviewers collectively confirm the paper's own honest framing: ICW is a genuinely novel concept that works well on capable models but faces a fundamental dependency on voluntary LLM compliance that cannot be guaranteed — it is a prerequisite, not a robustness property.

## Suggestions
- Fix or clarify the IPI equation at line 93 to resolve the apparent double-concatenation of the instruction.
- Add experiments on at least one model from a different provider (e.g., Claude, Gemini, or Llama 3.1) to validate the capability-scaling claim beyond OpenAI.
- Report per-sample compliance rates alongside aggregate ROC-AUC to characterize watermark reliability.
- Either replace the LLM-as-a-Judge with a calibrated metric or explicitly acknowledge the systematic bias where LLM text is rated higher than human text.

---

## Calibration Report

**Round 1 — Bracketing**

I searched six score bands with two queries ("watermarking LLM text detection prompt engineering black-box" and "LLM watermarking in-context learning robustness evaluation"). Here are all retrieved anchors:

| Path | Avg Score | Round | Comparison to ICW paper |
|------|-----------|-------|------------------------|
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | R1, band 1 | Less novel approach, rejected; ICW is more creative |
| xRi8sKo4XI (Unsupervised Prompt Learning) | 3.00 | R1, band 1 | Different topic (prompt tuning); ICW is stronger |
| kT6oc5CpEi (BlackDAN jailbreaking) | 3.00 | R1, band 1 | Unrelated topic |
| p4RAKZ4oik (FedDTPT) | 3.00 | R1, band 1 | Unrelated topic |
| 0koPj0cJV6 (A Watermark for Black-Box LMs) | 4.60 | R1, band 2 | Most directly comparable; ICW is more novel but similarly limited in experiments |
| eKGEsFdpin (I Know You Did Not Write That) | 3.67 | R1, band 2 | Watermarking method, less novel approach |
| fwHVclv0ij (Online Detection for Black-Box LLMs) | 5.25 | R1, band 2 | Different problem (change-point detection) |
| 0KHW6yXdiZ (End-to-End Logits Watermarking) | 5.25 | R1, band 2 | White-box approach; ICW is black-box, more broadly applicable |
| E4LAVLXAHW (Black-Box Detection of LM Watermarks) | 7.00 | R1, band 3 | Broader experiments, stronger methodology; ICW is less thorough |
| DEJIDCmWOz (Reliability of Watermarks) | 6.00 | R1, band 3 | Similar "initial exploration" scope; comparable contribution |
| KRMSH1GxUK (Watermarks for LLM IP) | 5.80 | R1, band 3 | Application-focused; ICW has more methodological novelty |
| LdIlnsePNt (Speculative Sampling Watermarking) | 6.00 | R1, band 3 | More theoretical; rejected at 6.0 despite being accepted range |
| j7b4mm7Ec9 (Lightweight Deep Watermarking) | 7.60 | R1, band 4 | Image watermarking; less related |
| 84n3UwkH7b (Memorization in Diffusion Models) | 8.00 | R1, band 4 | Unrelated (diffusion models) |
| Bo62NeU6VF (Backtracking Safety) | 8.00 | R1, band 4 | Unrelated (generation safety) |
| z8sxoCYgmd (LOKI Benchmark) | 8.00 | R1, band 4 | Unrelated (synthetic data detection) |
| ecbRyZZmKG (Double-I Watermark) | 5.25 | R1, band 5 | Fine-tuning watermarking; different approach |
| 3XTw909oXt (RAG Copyright) | 3.50 | R1, band 5 | RAG protection; less related |
| 5LhYYajlqV (In-Context Unlearning) | 5.33 | R1, band 5 | Different topic (unlearning) |
| 8o6LdeVi1K (WAPITI) | 3.75 | R1, band 5 | Fine-tuning watermarking; rejected |
| 9k0krNzvlV (Learnability of Watermarks) | 5.75 | R1, band 6 | Similar "initial exploration" scope; ICW is comparable |
| YPIA7bgd5y (In-Context Learning) | 6.50 | R1, band 6 | Different topic (ICL mechanisms) |
| ujpAYpFDEA (Can Watermarked LLMs be Identified) | 7.50 | R1, band 6 | First study on imperceptibility; more comprehensive eval than ICW |

**Round 1 bracket: 5.5–6.5**

The ICW paper is clearly more novel and better-motivated than the rejected 4.60 anchor ("A Watermark for Black-Box LMs"), which struggled with practicality concerns and presentation issues. It is comparable to the accepted 5.75–6.00 anchors ("On the Learnability of Watermarks," "On the Reliability of Watermarks," "Can Watermarks Detect LLM IP"), all of which are initial explorations of new watermarking questions with solid but limited experiments. The ICW paper is weaker than the 7.00+ anchors, which have broader experimental validation and more rigorous methodology.

**Round 2 — Narrowing**

I read the key anchors in detail:
- "A Watermark for Black-Box LMs" (4.60, reject): Mixed reviews (6,3,5,6,3), criticized for poor presentation and questionable black-box practicality. ICW is better written and has a cleaner motivating use case.
- "On the Reliability of Watermarks" (6.00, accept): Solid (6,6,6), focused on robustness with thorough experiments but acknowledged threat model limitations. ICW has more novelty but less experimental depth.
- "On the Learnability of Watermarks" (5.75, accept): Mixed quality (5,6,6,6), one reviewer saw limited novelty, another called it "experimental report." ICW is comparable in scope.
- "Can Watermarks Detect LLM IP" (5.80, accept): Application-focused (6,6,5,6,6), clear problem statement but limited model diversity — similar limitations to ICW.
- "Can Watermarked LLMs be Identified" (7.50, accept): Strong (8,8,6,8), first study on imperceptibility with comprehensive evaluation. Stronger than ICW.
- "Black-Box Detection of LM Watermarks" (7.00, accept): Strong (8,6,6,8), novel problem with rigorous methodology. Stronger than ICW.

The ICW paper's unique strengths over the 5.75–6.00 anchors include: (1) a genuinely new watermarking paradigm (prompt-based, no model access at all), (2) a compelling real-world application to peer review, and (3) better writing and presentation. Its weaknesses — limited model diversity, biased quality evaluation, compliance characterization — are comparable to the limitations that the 5.75–6.00 anchors were accepted despite having.

**Final score: 6.0** — The paper is a solid, novel contribution that establishes a new watermarking paradigm with a compelling use case. It's comparable to the accepted 5.75–6.00 anchors but would benefit from broader experimental validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have enough information to finalize my review. Let me compile the comprehensive analysis.

## Summary
This paper introduces In-Context Watermarking (ICW), a novel approach to embedding detectable watermarks into LLM-generated text purely through prompt engineering, without requiring access to model weights, logits, or decoding processes. Four strategies are proposed at different linguistic granularities (Unicode insertion, initial-letter biasing, lexical green-list biasing, and acrostics), each paired with a statistical detection method. Experiments on GPT-4o-mini and GPT-o3-mini validate the approach in both a Direct Text Stamp setting and an Indirect Prompt Injection setting motivated by detecting AI-generated academic reviews.

## Strengths
- **Novel paradigm that fills a clear gap:** ICW is, to my knowledge, the first method to embed watermarks entirely through prompt engineering with no model access. This is a distinct contribution from both in-process (logit-based) and post-hoc (paraphrase-based) watermarking, opening a new research direction.
- **Strong detection with capable models:** Table 2 shows that with GPT-o3-mini, all four ICW methods achieve DTS ROC-AUC ≥ 0.995 and IPI ROC-AUC ≥ 0.997, matching or exceeding PostMark (0.977) and YCZ+23 (0.998) — despite those baselines requiring model access.
- **Superior robustness under paraphrasing:** Figure 3 shows ICW methods maintain AUC 0.887–0.924 under paraphrasing attacks, while YCZ+23 drops to 0.557 (near chance). This demonstrates an inherent advantage of prompt-level watermarking for semantic-preserving attack models.
- **Preserved text quality:** Table 3 shows ICW methods maintain quality scores near unwatermarked output (4.81 vs. 4.99 overall), vastly outperforming PostMark (3.0) and even exceeding human-written text (4.24).
- **Well-designed multi-granularity design space:** The four ICW methods span Unicode/character/word/sentence levels with clear trade-off analysis (Table 1, Section 4 discussion), providing practitioners a principled basis for choosing.
- **Compelling real-world threat model:** The IPI setting for detecting AI-generated academic reviews is timely, practically motivated, and demonstrated to work empirically.

## Weaknesses

### Fatal
None.

### Major
- **Limited model diversity weakens core claims** — The abstract claims ICW is "model-agnostic" and that "as LLMs become more capable, ICW offers a promising direction," but experiments test only two OpenAI models (GPT-4o-mini and GPT-o3-mini). Different model families (Claude, Gemini, Llama, Qwen) have substantially different instruction-following profiles and system prompt handling. Moreover, GPT-o3-mini is a reasoning model with a fundamentally different training pipeline from GPT-4o-mini, so the performance gap cannot be attributed cleanly to "capability" rather than architecture differences. Testing across 4-5 model families would be needed to substantiate these central claims. (Verified: Table 2 shows only GPT-4o-mini and GPT-o3-mini; the abstract line 9 makes both claims.)

### Minor
- **No error bars or variance reporting** — All results in Tables 2, 3, and Figure 3 are single-point estimates. The green letter/word sets are randomly sampled, introducing variance. Without multiple-run reporting, readers cannot assess whether Initials ICW's 0.572 ROC-AUC on GPT-4o-mini versus 0.999 on GPT-o3-mini is reliable or seed-dependent. (Verified: Tables 2 and 3 present only single values.)
- **Text quality ceiling effect** — Unwatermarked GPT-o3-mini text scores 4.982–5.000/5.0 on all dimensions (Table 3), leaving minimal room for differentiation. While the 4.28–4.81 range for ICW does show variation, the ceiling compresses meaningful distinctions between methods. (Verified: Table 3, lines 267–276.)
- **Formula redundancy in IPI formulation** — Line 93 writes y ← M(t̃ ⊕ Instruction(k,τ) ⊕ Q), but t̃ is defined as t ⊕ Instruction(k,τ) on line 92, making the instruction appear twice. Should be y ← M(t̃ ⊕ Q). (Verified: lines 91-93.)
- **IPI practical assumptions untested** — The motivating scenario (embedding hidden instructions in PDFs for review detection) assumes PDF processing preserves white/zero-font-size text, that reviewers paste entire papers, and that LLMs follow the hidden instruction amid a full paper. The paper defers this to future work (Section 3.2, line 101) but provides no basic feasibility evaluation, making the IPI contribution more conceptual than validated. (Verified: Section 3.2.)

### Trivial
None.

## Nice-to-Haves
- Test on 2-3 additional model families (even DTS-only) to validate model-agnosticism and the capability-scaling narrative.
- Report standard deviations or confidence intervals across multiple random seeds.
- Improve text quality evaluation with pairwise comparisons or a wider rubric to avoid ceiling effects.
- Vary the 30% deletion/replacement attack parameter to show sensitivity curves rather than a single operating point.
- Include the "ignore prior prompts" attack evaluation in the main text (deferred to Appendix D.1), as it's critical to the IPI threat model.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Concerns about whether cited models exist — removed per hard rules (models cited are assumed to exist).
- Any formatting/style nitpicks about Table 1 symbols — removed per rules.
- Potential missing related works — removed per rules (cannot verify external existence).

## Novel Insights
The paper introduces a genuinely novel paradigm — embedding watermarks purely through prompt engineering without any model access — that fills a clear gap between in-process and post-hoc watermarking. The key empirical finding is that ICW robustness under paraphrasing significantly exceeds that of post-hoc baselines, suggesting prompt-level watermarking has inherent structural advantages for certain attack models. The capability-scaling observation (ICW effectiveness improving from GPT-4o-mini to GPT-o3-mini) is suggestive and directionally important, even if the limited model diversity prevents it from being fully validated.

## Suggestions
- Add experiments on 2-3 additional model families to substantiate the model-agnostic and capability-scaling claims.
- Report standard deviations or confidence intervals across multiple runs.
- Fix the IPI formula redundancy at line 93.
- Evaluate text quality with pairwise human comparisons to address ceiling effects.
- Add a basic IPI feasibility study with real PDF ingestion to validate the motivating scenario.

## Calibration Report

### All Anchors Retrieved

**Round 1:**
| Path | Avg Score | Band | Relevance |
|------|-----------|------|-----------|
| jbfDg4DgAk | 3.00 | Weak | LLM sparse watermarking — weaker concept, less novelty |
| vfEqSWpMfj | 2.50 | Weak | Word importance for prompt analysis — much weaker contribution |
| MV5j4Qpq7N | 2.33 | Weak | System-prompt jailbreak defense — unrelated area |
| OdoS6cH8MP | 2.00 | Weak | Textual data valuation — very different topic |
| 0koPj0cJV6 | 4.60 | Middle | Black-box watermark for LLMs — similar topic, but paper has more fragile practical setup |
| E4LAVLXAHW | 7.00 | Middle | Black-box detection of watermarks — stronger theoretical and empirical treatment, accepted |
| eKGEsFdpin | 3.67 | Middle | Sampling-based watermarking — weaker than ICW in novelty and results |
| DEJIDCmWOz | 6.00 | Middle | Reliability of LLM watermarks — accepted, comparable quality but different focus |
| j7b4mm7Ec9 | 7.60 | Strong | Lightweight deep watermarking (image domain) — less relevant |
| tTPHgb0EtV | 8.00 | Strong | Harmful fine-tuning defense — unrelated |
| 84n3UwkH7b | 8.00 | Strong | Diffusion memorization — unrelated |
| z8sxoCYgmd | 8.00 | Strong | Synthetic data detection — unrelated |

**Round 2:**
| Path | Avg Score | Band | Relevance |
|------|-----------|------|-----------|
| KRMSH1GxUK | 5.80 | Middle | LLM IP infringement via watermarks — accepted, comparable scope |
| FDfq0RRkuz | 5.50 | Middle | WASA source attribution — rejected, comparable scores but ICW is more novel |
| ecbRyZZmKG | 5.25 | Middle | Double-I watermark — rejected, less novel than ICW |
| qGLzeD9GCX | 4.25 | Middle | EditMark — rejected, less novel and weaker results than ICW |
| DEJIDCmWOz | 6.00 | Middle | Duplicate from Round 1 |
| KRMSH1GxUK | 5.80 | Middle | Duplicate from Round 1 |
| E4LAVLXAHW | 7.00 | Middle | Duplicate from Round 1 |
| LdIlnsePNt | 6.00 | Middle | SEAL watermarking — rejected despite comparable score; had serious proof issues but strong theory |

### Round 1 Bracket: 4.5 to 7.0

### Round 2 Narrowing: 5.0 to 6.0

### Comparison and Final Score

The paper under review is clearly stronger than EditMark (4.25, reject) and WASA (5.50, reject): ICW is more novel (new paradigm), has stronger empirical results (near-perfect AUC with GPT-o3-mini), and better addresses text quality and robustness. It is comparable to the Double-I watermark paper (5.25, reject), which also had a novel concept but weaker execution. The ICW paper is comparable in ambition to the LIDet/IP infringement paper (5.80, accept), which also proposes a novel application of watermarks but has its own evaluation limitations. However, ICW's evaluation is narrower (2 models from 1 provider) and its "model-agnostic" claims are less substantiated. Compared to the accepted "On the Reliability of Watermarks" (6.00), the ICW paper is less mature in its evaluation but more novel in its approach. Compared to SEAL (6.00, reject), ICW has fewer methodological flaws but also less theoretical depth.

The paper's novel concept and strong results with GPT-o3-mini place it above the 5.0-5.5 range, but the limited evaluation (2 models, no error bars, untested IPI assumptions) prevents it from reaching 6.0+. The ceiling effect in text quality evaluation is a real but minor concern. I score it 5.5: above the rejected papers at 5.25, comparable to the borderline 5.80 paper, but below the accepted papers at 6.0+.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
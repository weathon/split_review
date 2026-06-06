## Summary

This paper introduces **In-Context Watermarking (ICW)**, a method that embeds watermarks into LLM-generated text solely through prompt engineering, requiring no access to model weights, logits, or decoding processes. Four strategies are proposed (Unicode, Initials, Lexical, Acrostics ICW) and evaluated in a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) setting motivated by the problem of detecting AI-generated academic peer reviews. With GPT-o3-mini, all four methods achieve near-perfect detection (AUC ≥ 0.995 in DTS), and the IPI experiments demonstrate that covertly embedded watermarking instructions in long academic papers are reliably followed by capable LLMs.

---

## Strengths

- **Capability-dependent performance clearly demonstrated:** The paper shows a dramatic jump in detection performance when moving from GPT-4o-mini to GPT-o3-mini. For example, Initials ICW AUC goes from 0.572 to 0.999 and Acrostics from 0.590 to 1.000 (Table 2). Rather than hiding this, the paper frames it honestly as a capability-dependent mechanism, supporting the thesis that ICW will improve as LLMs advance.

- **IPI results are genuinely strong for capable LLMs:** Table 2 shows that with GPT-o3-mini, all ICW methods achieve ROC-AUC ≥ 0.997 in the IPI setting, demonstrating that LLMs reliably follow watermark instructions even when those instructions are embedded inside long (~8000-word) academic papers. This validates the core IPI feasibility claim.

- **Trade-off characterization across granularities:** The four strategies span different granularities and exhibit meaningfully different profiles (Table 1, Figure 3). Initials ICW achieves AUC 0.999 under word deletion/replacement; Lexical/Acrostics ICW achieve AUC 0.924/0.922 under paraphrasing; Unicode ICW is simple but fragile to LLM-based paraphrasing. This systematic comparison is useful.

- **Text quality well-preserved:** Table 3 shows ICW-watermarked text (with o3-mini) achieves relevance/quality/clarity scores of 4.808–4.813 overall vs. 4.992 for unwatermarked text, substantially outperforming PostMark (2.997) and competitive with human-written text (4.235). This is a practically important result.

- **Unique applicability in IPI settings:** The paper correctly identifies that post-hoc watermarking baselines (PostMark, YCZ+23) cannot be applied in the IPI setting because the dishonest reviewer controls no watermarking step. ICW is uniquely positioned to handle this scenario, and this is the paper's most differentiated contribution.

---

## Weaknesses

### Fatal
None.

### Major

- **Only two models from a single provider evaluated.** The experiments use only GPT-4o-mini and GPT-o3-mini (Section 5.1). While the paper's use of "model-agnostic" correctly refers to not requiring model internals (not that it works on any model), the extremely narrow model coverage limits the ability to generalize conclusions. With only two OpenAI models, it is unclear whether the results hold for other strong instruction-following LLMs (e.g., Claude Sonnet, Gemini Pro, or strong open-weight models like LLaMA-3-70B). The performance depends critically on instruction-following capability, but the paper provides no characterization of what capability threshold is required—it only observes that o3-mini works and 4o-mini largely does not. This is a structural gap given that the paper presents ICW as broadly practical.

- **IPI end-to-end pipeline not validated.** The paper's IPI mechanism depends on hidden text (zero-font or white-text in PDFs) being extracted by document processing pipelines and passed to the LLM's context. Section 3.2 describes this mechanism but the experimental evaluation treats IPI as equivalent to DTS with a prepended long-context document—it does not test whether hidden white text actually survives PDF-to-text conversion, API uploads, or UI drag-and-drop workflows. This is a feasibility question central to the use case. Figure 2 and its caption describe the mechanism, but the experiments never demonstrate it in a realistic document submission pipeline. If common PDF parsers strip zero-width or invisible text, the IPI mechanism fails before the LLM is ever involved.

### Minor

- **Three of four methods functionally fail with GPT-4o-mini.** Table 2 shows Initials ICW (AUC 0.572), Acrostics ICW (AUC 0.590), and Lexical ICW (AUC 0.910, T@1%F = 0.320) with GPT-4o-mini—effectively near-random or poor performance for three of four strategies. The paper acknowledges this, and it is consistent with the capability-dependent framing. However, the abstract and introduction describe ICW as "model-agnostic, practical" without immediately qualifying that currently only one of the two tested models yields reliable performance. The paper could be clearer that reliable operation currently requires frontier-level models.

- **Acrostics ICW detection has a potential statistical calibration issue.** In Section 4.2.4, the null distribution mean µ and std σ are estimated by resampling sentence-initial-letter sequences from the suspect text itself. If the text is heavily watermarked, the resampled sequences will be drawn from a biased distribution already shaped by ζ, which may affect null distribution calibration. The paper provides formal Type I error guarantees for Initials and Lexical ICW (Section 4.2.3) but explicitly does *not* make such a claim for Acrostics ICW—this asymmetry is unexplained and deserves acknowledgment.

- **Canterbury Corpus as background distribution for Initials ICW.** Section 4.2.2 uses the Canterbury Corpus to estimate the baseline initial-letter distribution γ. The Canterbury Corpus is general English prose, while evaluation is on ELI5 (long-form QA) and ICLR reviews—distinct genres. Genre-shifted γ estimates could miscalibrate the z-statistic. This is a minor concern but not flagged anywhere in the paper.

- **"Ignore prior prompts" attack relegated to appendix.** Section 5.2.1 acknowledges a "ignore prior prompts" adversarial attack in the IPI setting but reports results only in the appendix. Given that this is one of the most natural and easily deployed attacks in IPI scenarios, a brief summary in the main text would strengthen the paper's treatment of robustness.

### Trivial
None.

---

## Nice-to-Haves

- A characterization of "what model capability threshold enables reliable ICW"—the paper currently only shows two models at different ends of a performance cliff. Evaluating a few capability-graded models (e.g., GPT-4o, Claude Haiku/Sonnet, LLaMA-3-70B) and mapping performance against a capability measure would make the "as LLMs advance, ICW improves" thesis actionable and informative rather than qualitative.

- An end-to-end IPI demonstration with an actual PDF containing hidden text submitted through a realistic pipeline (e.g., API with PDF upload, or pasting extracted text), showing whether the instruction survives extraction and is followed.

- More explicit acknowledgment in the conclusion of the converse risk: highly capable models may also have stronger instruction-refusal mechanisms or system-level safeguards that could suppress hidden watermarking instructions.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic Issue #1 as framed (central claim "model-agnostic" unsupported):** The harsh critic interprets "model-agnostic" as "works across all models," but the paper uses the term to mean "requires no access to model decoding process." This is clearly stated throughout (Abstract: "solely through prompt engineering"; Section 3.1: "agnostic to the LLM M"). The "model-agnostic" framing is accurately supported—the method genuinely requires no model internals. The limited model breadth remains a real concern (retained above as Major), but the specific framing that the central claim is false is a misread.

- **Harsh Critic Issue #4 (baseline comparison "structurally misleading"):** The paper explicitly states that "when used with high-capability LLMs, ICW methods achieve detection performance comparable to that of the two baselines under the DTS setting." The DTS comparison with baselines is transparent, and the IPI setting's lack of baseline comparison is by design (baselines cannot apply). The framing that this is "structurally misleading" overclaims. The paper does not hide that GPT-4o-mini results are weaker—this is reported prominently in Table 2.

- **Strength Finder generic strength about "important problem":** Removed as this does not qualify as a concrete, paper-specific strength.

- **Harsh Critic claim that GPTZero is "absent from Table 2 and Figure 3":** The paper states GPTZero is a post-hoc baseline mentioned in the introduction as insufficient. The main results focus on the two black-box watermarking baselines. This appears to be a scope decision rather than an oversight. Removed as not clearly an error given the paper's framing.

---

## Novel Insights

The paper's most original observation is that LLMs' instruction-following capability can serve as a watermarking substrate—essentially turning an LLM's compliance into a detectable signal. The IPI threat model inversion (using a typically adversarial technique for a *defensive* purpose, with the conference organizer as the embedder and the dishonest reviewer as the inadvertent carrier) is a genuinely creative framing. The capability-dependence finding—that the performance cliff between GPT-4o-mini and o3-mini is extreme for instruction-complex methods (Initials: AUC 0.572 → 0.999)—is an empirically interesting and underappreciated phenomenon that could inform future work on benchmarking LLM instruction-following for watermarking purposes.

---

## Suggestions

1. **Evaluate at least 2–3 additional models** across families (e.g., Claude Sonnet, Gemini Pro, LLaMA-3-70B) to concretely support the model-generality claims and characterize the capability threshold for reliable ICW.
2. **Include an end-to-end IPI pipeline test:** demonstrate that hidden text in a real PDF survives extraction and is followed by the LLM in a realistic submission workflow.
3. **Add a brief main-text summary of the "ignore prior prompts" attack results**, since this is a key practical vulnerability in IPI.
4. **Formally discuss or experimentally calibrate** the Acrostics bootstrap null distribution under H₀ to provide at least empirical evidence of Type I error control.
5. **Clarify the "model-agnostic" terminology** in the abstract/introduction to avoid the reader conflating "no model access required" with "works on any model."

---

## Score and Decision

**Originality:** The ICW framing is genuinely novel—using prompting alone for watermarking, particularly the IPI repurposing of prompt injection as a defensive mechanism. No prior work has directly explored this angle.

**Importance:** Watermarking without model access is an important and underexplored problem. The peer-review abuse use case is timely and well-motivated.

**Claims supported:** Core claims about o3-mini performance are well-supported. Claims about breadth ("model-agnostic, practical") are qualified by limited model coverage. The IPI mechanism is demonstrated in-context but not end-to-end in a realistic PDF pipeline.

**Soundness:** The statistical detection methods for Initials and Lexical ICW are principled. The Acrostics method has a minor calibration concern. Experiments are clean and transparent.

**Clarity:** Writing is clear. The paper is honest about limitations. The Table 1 trade-off summary is helpful.

**Community value:** The IPI framing, capability-dependence analysis, and trade-off characterization provide genuinely useful signals for the watermarking and LLM communities.

Overall: this is a well-executed initial exploration of a novel direction with honest reporting and strong o3-mini results. The major gaps (model breadth, IPI pipeline validation) are real but characteristic of early work establishing feasibility; they do not invalidate the contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
Now I have a thorough understanding of the paper, the reviewer inputs, and the calibration anchors. Let me write the consolidated review.

---

## Summary

This paper investigates how the well-studied IOI circuit in GPT-2 small generalizes to prompt variants (DoubleIO, TripleIO) that violate the assumptions of the IOI algorithm. The authors find that (1) the base IOI circuit outperforms the full model on these variants due to an artifact of the ablation procedure they term "S2 Hacking," and (2) when new circuits are discovered for the variants using standard path patching, they **reuse 100% of heads** and 85–92% of edges from the base IOI circuit, adding only new input edges to handle duplicated IO tokens. The paper also identifies a "first come, first serve" decision point in head 2.2 that helps resolve which duplicate to suppress.

## Strengths

- **Quantified circuit reuse with near-complete overlap.** Table 2 reports that newly discovered circuits for DoubleIO and TripleIO have 100% node overlap with the base IOI circuit and edge overlaps of 91.66% and 84.61%, rising to faithfulness of 0.765–0.778 after adding 10–20 new edges. This is concrete, well-measured evidence for the "strong generalization" scenario (component reuse with minimal structural additions), and goes beyond prior work that noted circuit overlap only qualitatively (Hanna et al., 2023; Wang et al., 2023).

- **Mechanistic tracing of S2 Hacking.** Section 4 traces a concrete causal cascade from Duplicate head 3.0 through Induction heads 5.5/5.9 to S-Inhibition head 8.6, using confidence ratio and functional faithfulness metrics (Figure 4). The paper is transparent that this is a byproduct of the knockout procedure ("not actually how the full model solves the task," line 200), but the mechanistic account of *why* and *how* the circuit outperforms the model is still a valid and useful finding for researchers studying circuit evaluation.

- **Most attention heads show minimal deviation from base IOI behavior.** Figure 2 shows that Name Mover heads and most other heads deviate by less than 0.1 in attention scores between base IOI and the variants, providing evidence that the components retain their core functionality under prompt changes.

- **Systematic edge-addition analysis.** Figure 5 presents a clean ablation: adding paths from IO2 (and IO3 for TripleIO) to the Duplicate and Previous Token heads progressively brings faithfulness from 1.285/2.586 down to 0.765/0.778, methodically identifying which additional input edges are causally necessary.

- **Identification of a decision-point head.** Figure 8 shows that Previous Token head 2.2 attends far more to the name that appears first in the prompt (0.56 vs 0.27 when IO first; 0.57 vs 0.26 when S first), providing a concrete mechanism for how the model resolves duplicate ambiguity in the DoubleIO variant.

## Weaknesses

### Fatal

None.

### Major

- **Single model, single task limits the scope of the "circuits are more flexible" claim.** All experiments are on GPT-2 small and the IOI task only. The abstract and conclusion claim that "circuits within LLMs may be more flexible and general than previously recognized" (Abstract) — this extrapolation from a single case study is not supported. It is entirely possible that other circuits (e.g., Greater-Than, modular arithmetic, or IOI in larger models) would show different generalization behavior. The paper would be stronger with experiments on at least one other model or task, or with claims scoped explicitly to the IOI circuit in GPT-2 small.

### Minor

- **The head 2.2 "first come, first serve" analysis is correlational, not causal.** The analysis (Section 5.3, Figure 8) is based on average attention scores. There is no intervention (e.g., mean ablation or activation patching of head 2.2) to demonstrate that this head *causes* the order-dependent performance difference. The paper acknowledges that a "more detailed study of the duplicate suppression mechanism is left to future work" (line 349), but without a causal test the "decision point" claim remains a correlation. This limits the strength of what would otherwise be the most novel finding in the paper.

- **The framing oscillates between two different meanings of "generalization," which could confuse readers.** The abstract and introduction present a unified narrative ("the circuit generalizes surprisingly well"), but the paper actually makes two separable claims: (a) the *base* IOI circuit performs well on variants (Section 3, explained by S2 Hacking in Section 4), and (b) the *newly discovered* circuits for the variants reuse all base-circuit components (Section 5, the genuine generalization finding). Claim (a) is an artifact of the ablation procedure, which the paper correctly notes, but it is presented alongside the reuse claim without clear demarcation. For instance, the Introduction says "the IOI circuit vastly outperforms the full model on prompt variants" (line 41) without immediately clarifying that this refers to the base circuit operating under mean ablation. The paper would be clearer if it explicitly separated these two narratives: first a cautionary result about circuit evaluation on OOD inputs, then a positive result about component reuse.

- **The circuit discovery procedure for the variants could be more precisely specified.** While the paper states it follows Wang et al. (2023)'s methodology (Section 5.2), the description does not report the threshold used to determine "significant" causal effect for edge inclusion, how token-level effects are aggregated across different token positions, or whether any alternative edges outside the base IOI circuit were tested and rejected. The circuits were clearly discovered with guidance from the known base IOI circuit structure (starting from it and adding edges). This is a reasonable approach, but the paper should explicitly state whether the search was exhaustive or guided, and what criteria were used for inclusion.

### Trivial

None.

## Nice-to-Haves

- Validating head 2.2 with a causal intervention (e.g., mean ablating it and showing the order-dependent effect disappears) would significantly strengthen the decision-point finding.
- Adding experiments on a second model (e.g., GPT-2 medium or a Pythia model) would substantially broaden the paper's claims.
- Reporting confidence intervals for the key logit differences in Table 1 and Table 2 would improve the presentation.

## Removed Points

These points from the input reviews are not included as weaknesses in the main review above. They are recorded here for transparency.

1. **"S2 Hacking is an artifact of the evaluation protocol, not a discovery"** — REMOVED. The paper explicitly states this: "Note that this phenomenon only occurs in the base IOI circuit, as it is a byproduct of the knockout procedure... and not actually how the full model solves the task" (line 200). The paper's contribution is discovering and mechanistically explaining *why* the artifact occurs, which is valid.

2. **"Generalization claim is contradicted by unfaithfulness evidence"** — REMOVED. The paper's "generalization" claim in the abstract ("reusing all of its components and mechanisms") refers to the circuit-reuse finding in Section 5 (Table 2: 100% node overlap), not to the base circuit being faithful on variants. The paper acknowledges the base circuit is unfaithful (Table 1 caption: "faithfulness is far from the ideal value of 1"; line 101: "the performance of the base IOI circuit on the prompt variants is not faithful").

3. **"Missing confidence intervals"** — REMOVED. The paper states: "all metrics are plotted with confidence intervals based on 50 samples" (line 210, referring to Figure 4). While Table 1 and Table 2 do not show CIs, the core diagnostic figure does.

4. **"Missing control for S2 Hacking"** — REMOVED. The paper's entire analysis of S2 Hacking (Section 4) is a mechanistic trace of how the knockout procedure causes the behavior. A random knockout control would trivially confirm what the paper already demonstrates.

5. **"Circuit discovery is underspecified"** — PARTIALLY ADDRESSED (demoted to Minor). The paper follows the established Wang et al. (2023) methodology. Thresholds and search strategy details could be added but the method is not fatally underspecified.

6. **"Missing related work"** — REMOVED per policy (cannot verify existence of absent references).

7. **"Missing appendix/proofs"** — REMOVED per policy (parser strips these from all submissions).

8. **Generic formatting/presentation nitpicks** — REMOVED per policy.

## Novel Insights

None beyond the paper's own contributions. The dual finding — that the base IOI circuit's high performance on variants is an ablation artifact (S2 Hacking) while simultaneously the circuit components genuinely are reused in the model's actual solution — is interesting but is exactly what the paper presents.

## Suggestions

1. **Reframe the two narratives clearly.** Separate the cautionary S2 Hacking finding ("circuit evaluation on OOD inputs can produce spurious results") from the positive circuit-reuse finding ("the model's actual solution for variants reuses all base IOI components"). This would make the paper's dual contribution clearer and avoid the framing tension.

2. **Add a causal intervention for head 2.2.** Even a simple mean ablation experiment showing that removing head 2.2 eliminates the order-dependent performance difference would elevate this from a correlational observation to a validated mechanism.

3. **Scope the claims to match the evidence.** Replace "circuits within LLMs may be more flexible and general than previously recognized" with a claim specific to the IOI circuit in GPT-2 small, such as "the IOI circuit in GPT-2 small exhibits stronger generalization through component reuse than previously documented."

4. **Specify the circuit discovery thresholds.** State the exact causal effect threshold (e.g., in % logit difference) used to include a head or edge in the DoubleIO/TripleIO circuits, and clarify whether the search was exhaustive over all heads or guided by the base circuit structure.

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Three queries on "mechanistic interpretability circuit generalization IOI GPT-2" with score bands (-∞, 3.5), (3.5, 7.5), (7.5, ∞).

**Round 1 anchors:**
- `fM1ETm3ssl.md` — avg 3.00 (reject): Automated interpretability via meta-models. Weaker execution, unclear contribution.
- `73dhbcXxtV.md` — avg 3.00 (reject): Logic-language framework paper. Poorly motivated.
- `89wVrywsIy.md` — avg 3.40 (withdrawn): SAE-based hierarchical tracing. Lacked faithfulness evaluation.
- `fSbPwHjdDG.md` — avg 3.00 (reject): Causal interventions on Llama language. Different topic.
- `JZjW3k4Kyc.md` — avg 3.75 (withdrawn): Circuit transformations across inputs/fine-tuning. Very mixed reviews (1,8,3,3); unclear contribution.
- `VwyKSnMmrr.md` — avg 4.67 (withdrawn): Language skill circuits. Had technical errors.
- `sZq3lDDETp.md` — avg 4.20 (withdrawn): Circuit probing. Different topic.
- `5IWJBStfU7.md` — avg 7.00 (accepted poster): MI identifiability. Stronger theoretical contribution, broader scope.
- `I4e82CIDxv.md` — avg 8.00 (accepted oral): Sparse feature circuits. Significantly stronger.
- `aN4Jf6Cx69.md` — avg 9.00 (accepted oral): Mechanistic basis of ICL. Much stronger.
- `gc8QAQfXv6.md` — avg 9.00 (accepted oral): Function vectors for forgetting. Different topic.
- `STUGfUz8ob.md` — avg 7.60 (accepted poster): Transformers reasoning with symbols. Stronger.

**Round 1 bracket:** plausible range = 4.0–6.0.

**Round 2 — Narrowing.** Queries on (3.5, 6.0) and (5.0, 7.5) bands for related topics.
- `w4gkS9RsWh.md` — avg 4.50 (withdrawn): Memorization vs. generalization detection. Limited scope, weak technical contribution.
- `rkfiJQMFcw.md` — avg 5.50 (reject): DNA trace reconstruction. Different topic.
- `hPk92D2GJV.md` — avg 5.25 (reject): Context vs. internal knowledge. Different topic.
- `ekeyCgeRfC.md` — avg 7.00 (accepted oral): ICL in transformers. Much stronger theoretical work.

**Comparative assessment:** The paper under review is clearly stronger than the 3.0–3.75 anchors (which had unclear contributions, technical flaws, or missing evidence). It is comparable to or slightly stronger than the 4.5–4.67 anchors (w4gkS9RsWh.md, VwyKSnMmrr.md), which were limited in scope or had technical issues. However, it is substantially weaker than the 7.0+ anchors (5IWJBStfU7.md, I4e82CIDxv.md), which have broader theoretical contributions, multiple models, or more rigorous validation. The paper's primary limitation is its single-model single-task scope and the preliminary nature of the decision-point finding.

**Final score:** 5.0 — a solid empirical contribution with clear findings, but limited in scope and with some framing issues. The evidence supports the component-reuse claim well, but the broader claims about circuit flexibility are not justified by the data. The paper is below the acceptance threshold for a top venue in its current form, but the core findings (circuit reuse quantification, S2 Hacking mechanism) are publishable with revisions that scope claims appropriately.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
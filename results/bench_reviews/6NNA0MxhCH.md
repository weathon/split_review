Now let me run the calibration search to anchor my score.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary
This paper investigates the internal mechanisms by which transformer language models perform formatted multiple-choice question answering (MCQA). Using vocabulary projection and activation patching on two model families (Olmo-7B-SFT and Llama2-13B-Chat), the authors localize answer symbol production to a small number of middle-to-late layers dominated by a sparse set of specialized attention heads. The paper additionally introduces a synthetic Colors task to disentangle MCQA formatting ability from domain knowledge, and finds evidence that poorly-performing checkpoints fail to separate answer symbols in vocabulary space.

---

## Strengths

- **Principled model selection via consistency criterion**: The four-prompt design (AB-A-correct, AB-B-correct, CD-C-correct, CD-D-correct) provides a clean operationalization of robustness to position and symbol, and the ≥70% threshold is well-motivated. This is a methodological contribution that prior work lacked.

- **Complementary use of two methods**: The paper makes a coherent and substantive argument (Section 4) that vocabulary projection and activation patching reveal *different and compatible* aspects of the same process—activation patching uncovers causal contributions before hidden states are projectable to vocabulary space, while vocabulary projection tracks probability buildup in subsequent layers. This is the paper's most methodologically coherent insight.

- **Two-stage C/D processing in Olmo-7B-SFT**: The finding that Olmo-7B-SFT processes out-of-distribution symbols (C/D) by first promoting in-distribution symbols (A/B) and abruptly switching at layer 30 is the paper's most novel empirical contribution. Convergent evidence from both vocabulary projection (Figures showing C/D patterns) and activation patching (Fig. showing layers 21–29 closing the A/B gap before layer-30 switch) gives this finding real credibility.

- **Synthetic Colors task as a diagnostic**: Because all models succeed at generative Colors (100% accuracy on color-string generation), failures on formatted MCQA are attributable specifically to symbol binding, not factual knowledge. This is a clean diagnostic that allows the paper to isolate and track exactly when formatted MCQA capability emerges during Olmo-v1.7 training (between 350B and 1T tokens).

- **Sparse, specialized attention heads**: The identification of ~8–13 attention heads dominating answer symbol production and the four-type specialization taxonomy (always-A, always-B, correct-letter, B-only-activating), with 100% overlap between components promoting total probability and discriminative components, is a concrete and reproducible finding.

---

## Weaknesses

### Fatal
None.

### Major

- **Abstract overclaims "a single middle layer" — a finding that does not hold for both studied models.** The abstract states: *"prediction of a specific answer symbol is causally attributed to a single middle layer."* This is accurate for Olmo-7B-SFT (Layer 21 is sharply causal), but Section 4 explicitly acknowledges for Llama2-13B-Chat: *"we observe a more diffuse window of ~6 layers (15-21) at which activation patching is increasingly able to change the model's prediction."* A six-layer diffuse window is categorically different from a single layer. The headline claim of the abstract, Figure 1, and the introduction is therefore imprecise at best and misleading at worst. This requires either qualification ("in at least one model") or a substantive theoretical argument for equivalence.

- **All mechanistic findings rest on exactly two models, while the paper claims general insights into "how LMs answer formatted MCQA."** After applying the consistency criterion, mechanistic analysis is restricted to Olmo-7B-SFT and Llama2-13B-Chat. These two models already show meaningfully different behaviors (sharp vs. diffuse localization; two-stage vs. direct C/D processing). The paper frames findings as general—the abstract uses "LMs," not "two models"—but a finding from two model families cannot support that generality. A third model family (e.g., Mistral or Phi) would begin to establish or refute generality.

- **Binary MCQA analysis is mismatched to the paper's stated motivation.** Section 3.1 converts all datasets to 2-choice binary MCQA with explicit justification (discriminativity metric). However, the paper's introduction cites MMLU, HellaSwag, and formatted MCQA benchmarks that are 4-choice. The paper does not test whether any mechanistic finding (which layer is causal, how many heads are active, the C/D two-stage behavior) transfers to the 4-choice format. The selection mechanisms for 2-choice (distinguish A vs. B) may structurally differ from 4-choice (rank four options). This gap directly undermines the connection between the mechanistic findings and the benchmarks that motivate the work.

### Minor

- **The activation patching confound between letter identity and answer position is not addressed.** The two patched prompts (AB-A-correct and AB-B-correct) differ simultaneously in (a) which letter is the correct answer symbol *and* (b) the text position of the correct answer choice. Activation patching cannot cleanly attribute the effect to "answer symbol selection" vs. "answer position encoding" because both co-vary. This is particularly important for the claim that the localized layers drive "answer symbol production." The authors should discuss this confound even if it is difficult to fully disentangle.

- **The two-stage C/D interpretation is purely observational.** The paper presents vocabulary projection and activation patching as convergent evidence that Olmo-7B-SFT first promotes A/B before switching to C/D at layer 30. This is plausible and interesting. However, no intervention tests the causal necessity of the A/B intermediate representation—for example, ablating or suppressing the layer-21 signal during C/D prompts to determine whether the model can "skip" to C/D directly or fails. Without this, the two-stage description remains descriptive rather than mechanistically verified.

- **The mechanistic depth of the attention head analysis is limited to "what" rather than "how."** Section 5 establishes *that* ~8–13 heads promote specific symbols but not *what those heads attend to* in the input. Lieberum et al. (2023), already cited, showed that "correct letter heads" attend to answer symbol tokens at earlier positions. Whether the paper's identified heads have the same property, a different one, or a novel mechanism is unanswered. This gap leaves the specialization taxonomy as descriptive rather than mechanistic.

- **The Colors test set is small (105 instances).** The core "inability to separate" finding for poorly-performing checkpoints and the characterization of the training transition (350B→1T tokens) rest entirely on 105 test instances. While the Colors task is synthetic and the effect sizes appear large, this is a thin empirical base for the generalized causal claim in the abstract's last sentence.

### Trivial
- The in-context examples always use fixed label distribution A, B, B. The sensitivity of mechanistic findings to this fixed prior is never tested, though the consistency design partially addresses positional bias at the model-selection level.

---

## Nice-to-Haves

- Replicate the core mechanistic analysis (activation patching localization, head specialization) on the 4-choice MCQA format. Even a partial demonstration would close the gap between analysis format and benchmark motivation.
- Visualize what the identified key attention heads attend to (cf. Lieberum et al.'s methodology), to move from "which heads promote A/B" to "why they promote it."
- Extend consistency analysis and mechanistic investigation to one additional model family to begin establishing or refuting generality.
- Provide failure-case vocabulary projection traces (where the model applies the same mechanism but selects the wrong symbol) to separate mechanism failures from information failures.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Fixed A, B, B in-context prior creates label bias"** (Harsh Critic): The paper acknowledges label bias as one of the motivating concerns, and the consistency criterion explicitly tests robustness to positional and symbol variations. The choice of A, B, B is a design convenience and the paper's core controls account for positional/label bias. This concern is partially addressed and not severe enough to keep as a weakness.

- **"Olmo v1.7's ability to do symbol binding doesn't alleviate separability on harder datasets"** (Harsh Critic): This is actually a *finding* of the paper, not a weakness—the paper explicitly reports it as evidence that the synthetic task is a useful diagnostic. Moving this to the removed section as a misclassified observation.

- **Strength Finder: "Paper addresses an important problem"** (Generic): Removed as insufficiently concrete; MCQA benchmark evaluation is broadly important but this is generic praise.

- **Strength Finder: "Diagnosis of poor performance as inability to separate answer tokens"**: Partially preserved but weakened above by the small Colors test set. The finding is real but requires epistemic humility about how far it generalizes.

---

## Novel Insights

The most genuinely novel insight is the two-stage hypothesis for C/D symbol processing: Olmo-7B-SFT does not directly compute the correct out-of-distribution symbol but instead routes through the A/B symbol space before an abrupt late-layer redirection. This is both a specific mechanistic claim and a potential explanatory framework for why some models fail catastrophically under format perturbations while others do not. The contrast with Llama2-13B-Chat (which directly promotes C/D) suggests this may be a training-data or fine-tuning artifact worth pursuing further. The paper also makes a useful diagnostic contribution with the Colors synthetic task, which could become a standard lightweight probe for studying when and how formatted MCQA capability is acquired during pretraining.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: Moderate-to-good. The combination of vocabulary projection + activation patching for MCQA is novel, and the two-stage C/D finding and Colors diagnostic are original. However, the head specialization finding extends Lieberum et al. without going substantially deeper mechanistically.
- *Importance*: Good. Formatted MCQA is a central evaluation paradigm, and understanding its internal mechanisms is genuinely useful.
- *Claim support*: Weak-to-moderate. The headline claim (single layer) doesn't hold uniformly; the generalizations are calibrated for "LMs" but evidenced only for two models; the binary format limits connection to the stated benchmarks.
- *Soundness of experiments*: Good, with the noted confound (letter vs. position) and the observational nature of the two-stage claim.
- *Clarity*: Good overall. The paper is well-organized, figures are informative.
- *Value to community*: Moderate. The findings are interesting but the overclaiming and scope limitations reduce their immediate utility.

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/A0W7VCSQev.md` (MCQA attention heads) | 4.75, Reject | Most topically similar. That paper also uses attention heads for MCQA and is rejected for limited generalization and incomplete baselines. The paper under review has stronger mechanistic analysis but similar generalization concerns. |
| `/Pw7Wb3dGvg.md` (Llava VQA mechanistic) | 3.50, Reject | Single model, one task type, limited novelty over prior work. The paper under review is clearly stronger: multiple models, multiple datasets, more original findings. |
| `/g8oaZRhDcf.md` (Copy suppression attention head) | 5.00, Reject | More mechanistically rigorous (full explanation of one head), single model (GPT-2 Small). Paper under review is broader, slightly less deep. Comparable quality. |
| `/AwyxtyMwaG.md` (Function vectors) | 6.00, Accept | Function vectors tests across many more tasks and models, finds a more elegant and broadly applicable finding. Paper under review has similar methodology but narrower scope and more overclaiming. |
| `/Hf17y6u9BC.md` (Activation patching best practices) | 6.67, Accept | More methodological contribution; more systematic; addresses the very confounds the paper under review overlooks. Paper under review is weaker on methodology. |
| `/IRvx66cxip.md` (Enhanced IG + attention) | 2.75, Reject | Much weaker; lacks rigorous mechanistic analysis. Paper under review is substantially better. |
| `/JBLHIR8kBZ.md` (Neuron to Graph) | 4.00, Reject | Superficial interpretability; less rigorous. Paper under review is stronger. |
| `/Ayf42Bo6sk.md` (Token-level semantic dependencies) | 4.00, Reject | Superficial mechanistic claims; less clean experimental design. Paper under review is stronger. |

The paper under review sits between the rejected `g8oaZRhDcf.md` (5.0) and the accepted `AwyxtyMwaG.md` (6.0). The overclaim in the abstract, the two-model scope, and the binary-vs-4-choice mismatch are genuine problems that pull it below the function vectors paper. But it is clearly better than the 4.0-4.75 rejected papers. The major weaknesses are real and would require revision to fully address, but they don't invalidate the paper's core contributions.

**Final score: 5.0** — The paper makes genuine and interesting mechanistic contributions to a well-motivated problem, but the scope of claims significantly exceeds the evidence (two models, binary format, one model showing "single layer"), and the mechanistic depth stops at description rather than explanation. These issues place it at the borderline.

**Decision: Reject (weak reject)** — The findings are interesting and the experimental design is creative, but the combination of the headline overclaim, two-model scope, and the binary-vs-4-choice mismatch with the stated motivation is significant enough to require revision before acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
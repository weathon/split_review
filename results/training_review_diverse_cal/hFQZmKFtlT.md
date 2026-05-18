Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper develops a clean experimental framework using formal grammars (random and hierarchical) to disentangle two modes of learning in LLMs: memorization (rote) and generalization (understanding). By fine-tuning Pythia-1B, Llama3-8B, and Mistral NeMo-12B on grammar-generated strings with full control over data distributions, the authors make several empirical observations: (1) training passes through distinct generalization and memorization phases that can overlap; (2) memorization harms generalization and vice-versa, with sequential training on new data causing forgetting of previously memorized strings; (3) lower-entropy distributions favor generalization while higher-entropy distributions favor memorization; and (4) measuring training-set recollection alone cannot determine whether a model has memorized—comparison to an unseen test set is necessary.

## Strengths

- **Clean, well-controlled experimental framework using formal grammars.** The paper designs training and evaluation with random and hierarchical grammars, providing full control over data distributions, syntax, and entropy, enabling precise measurement of when memorization and generalization occur. Test data is guaranteed unseen and identically distributed. This framework is described in Section 2 and used consistently across all experiments (Figures 2–5).

- **Clear empirical demonstration that rote learning and generalization are antagonistic.** The paper shows that once the memorization phase begins, test loss increases (generalization worsens). The sequential memorization experiment (Section 4, Figure 4) directly shows that memorizing a second dataset causes loss on the first to rise back to test level, supporting the antagonistic interplay. This result is replicated across all three model families.

- **Entropy is shown to differentially affect generalization vs. memorization.** The paper systematically varies entropy in three independent ways (alphabet size, token oversampling, production rule skewness) and finds consistent patterns: lower-entropy distributions yield better generalization but slower memorization, while higher-entropy distributions are memorized more quickly (Figure 5). The consistency across three manipulations and three model families is convincing.

- **Demonstration that memorization cannot be measured from recollection alone.** The paper provides a concrete counterexample (Figure 3) where two models achieve the same training loss but one is in the memorization phase and the other in the generalization phase. This directly challenges prior definitions that rely solely on training-set recollection (Carlini et al., Tirumala et al.) and supports the paper's claim that measuring memorization requires comparison to an unseen test set.

- **Validation across model families and scales.** Core findings are replicated on Pythia-1B, Llama3-8B, and Mistral NeMo-12B—spanning different architectures and an order of magnitude in parameter count—strengthening the generality of the conclusions (Figures 2, 4, 5).

- **Clear operational definitions.** The paper introduces reproducible definitions: memorization starts when test loss exceeds training loss by 5% (cross markers); generalization ends at the epoch of minimum test loss (triangle markers). These are used consistently throughout the paper.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The 5% threshold for memorization onset is not justified.** The paper defines the start of memorization as the epoch where `Loss(test) > 1.05 × Loss(train)`, but no rationale is given for this specific value. While the qualitative pattern of divergence is robust, precise claims about *when* memorization starts (e.g., "epoch six" in Figure 1) and the analysis of phase boundaries in Section 3.1 are threshold-dependent. A brief discussion of sensitivity to this choice would strengthen the methodology.

- **The potential confound of pretrained representations is acknowledged but not fully addressed.** The paper fine-tunes models that were pretrained on natural-language corpora. These models enter the experiment with prior knowledge of token distributions, character co-occurrences, and sequential patterns that could plausibly influence the speed of generalization or the onset of memorization. The paper's claim that the grammar strings were "not seen during pre-training" (Section 1) addresses data overlap but not the influence of prior distributional knowledge. However, this concern is substantially mitigated by the consistency of the observed dynamics across three model families (Pythia, Llama, Mistral) with very different pretraining data, suggesting the phenomena are not artifacts of a specific pretraining corpus. The paper would benefit from an explicit discussion of this point rather than mentioning it only indirectly through the synthetic-data limitation.

- **The sequential forgetting result would benefit from sharper interpretation.** The paper states that "memorizing new data from the same distribution causes forgetting of previously memorized data." However, as shown in Figure 4, the loss on the first training set rises to approximately match the test loss, not above it—meaning the model retains distributional understanding (generalization) while losing recall of exact training strings. This distinction between forgetting rote recall vs. forgetting distributional knowledge is important and could be discussed more explicitly, as it suggests that forgetting is selective to memorized training strings, not to the learned distribution.

### Trivial

- The proposed contrastive memorization measure (Equation 1: `1 − Loss_train / Loss_test`) is introduced in Section 3.2 but not applied in any subsequent analysis. The paper explicitly frames this as future work, so this is not a flaw, but the measure's utility remains a suggestion rather than a demonstration. Adding a simple illustrative analysis (e.g., showing how it evolves over training for one model) would make the proposal more concrete.

## Nice-to-Haves

- **A random initialization control experiment.** Training the same architectures from random initialization on the grammar data (or using a token set sufficiently different from natural-language pretraining) would further isolate whether the observed dynamics are properties of the optimization procedure and architecture or are influenced by pretrained representations. The consistency across model families already addresses the core concern, but such an experiment would definitively rule out the pretraining confound.

- **Computing existing memorization metrics (Carlini et al.'s 50-token extraction, Tirumala et al.'s per-token accuracy) on the same models shown in Figure 3.** While Figure 3 conceptually demonstrates the problem, a concrete comparison table showing how the same models would be classified by existing metrics vs. the paper's loss-based criterion would make the critique actionable.

- **Sample-level analysis of which specific training strings are memorized first.** Investigating whether memorization is concentrated on low-probability outliers under the grammar would deepen the entropy findings.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No analysis of token-level accuracy is reported in the main body"** — REMOVED (factually incorrect). Figure 1 explicitly reports "Training and test loss **and accuracy** for the Llama3-8B model on the hierarchical grammar." Accuracy is shown in this main-body figure. The claim that accuracy is entirely absent is false.

- **"Learning by rote vs. with understanding framing is sloppy"** — REMOVED (misunderstands the paper). The paper provides clear operational definitions in Section 3.1: "learning by rote" corresponds to the memorization phase (test loss diverges from training loss); "learning with understanding" corresponds to the generalization phase (test loss decreases with training loss). The thought experiment in the introduction establishes the intuition. The operationalization is precise and reproducible.

- **"Pretrained model confound as a fatal/generalizability threat"** — DOWNGRADED from the critic's framing. The critic presents this as undermining the paper's core claims about "LLMs as a class." However, the paper studies LLMs *as they are actually used* (i.e., starting from pretrained weights), and the consistency of results across three model families with different pretraining data (Pythia trained on The Pile, Llama on web data, Mistral on diverse corpora) provides strong evidence that the observed dynamics are not artifacts of a specific pretraining corpus. This is a minor limitation, not a fatal flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an original observation that the paper itself does not already make or clearly imply.

## Suggestions

1. **Add a brief sensitivity analysis for the 5% divergence threshold.** Show that the qualitative pattern of phase overlap, sequential forgetting, and entropy effects holds for a range of reasonable thresholds (e.g., 2%, 5%, 10%). This would address the main methodological concern without requiring new experiments.

2. **Explicitly discuss why pretraining is unlikely to drive the observed dynamics.** Add 2–3 sentences noting that the consistency across model families with different pretraining data argues against the concern that prior token/character knowledge determines the phase boundaries, and that the core claims are about LLMs as used (starting from pretrained weights).

3. **Refine the interpretation of the sequential forgetting result.** Explicitly note that the loss on the first training set rises to match the test loss (not exceed it), indicating that forgetting is selective to rote recall of exact training strings while distributional understanding is retained.

## Score and Decision

Based on my assessment: the paper presents a clean, well-executed empirical framework with genuinely novel findings (antagonistic phase dynamics, entropy-dependent learning, sequential forgetting) validated across multiple model families. The weaknesses are minor—they concern threshold justification, framing sharpness, and a mitigated pretraining confound—and do not threaten the core claims. This is a solid empirical contribution to the understanding of memorization in LLMs.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
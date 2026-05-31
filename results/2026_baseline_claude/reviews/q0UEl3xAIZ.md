## Summary
This paper applies Goal-Oriented Environment Inference (GOEI), a model-based RL algorithm previously published by the same group (Takahashi et al., 2024), to a competitive card game "Hol's der Geier" to validate its state-reduction capability in a more realistic setting. GOEI learns a reduced Markov state space (452 states, 2.9% of the 15,542 possible observations) using Dirichlet process-based variational Bayesian inference and achieves performance nearly equivalent to the Nash equilibrium. The paper also provides an information-theoretic analysis of which game features are preserved or discarded by the state reduction.

---

## Strengths

- **Clear and verifiable evaluation criterion.** Hol's der Geier has a computable Nash equilibrium, providing an objective, ground-truth benchmark. Achieving reward rate ≈ 0 against the NE opponent is a meaningful and falsifiable claim.
- **Striking state compression.** Reducing 15,542 observations to 452 states (2.9%) while maintaining near-optimal performance is a quantitatively impressive result, clearly documented in Table 1 and Figure 2.
- **Informative mutual information analysis (Section 4.2).** Decomposing retained information by feature (SD, CT, AH, OH, RT) and round gives concrete evidence of what GOEI preserves; e.g., the finding that score difference (SD) becomes relevant only at late rounds matches game-theoretic intuition.
- **Thorough parameter sensitivity analysis.** Section 4.3 provides interpretable hypotheses about α (Dirichlet process concentration) and β (Dirichlet distribution sparsity), confirmed experimentally across a 3×3 grid of settings.

---

## Weaknesses

### Fatal
None. The core empirical claims appear sound.

### Major

1. **Core algorithm is not novel to this submission.** GOEI is drawn entirely from Takahashi et al., 2024 (Neural Networks). This paper is exclusively a validation study of that prior work on a new environment. There is no algorithmic, theoretical, or methodological contribution beyond application. For a research venue like ICLR, which expects new knowledge, this is a substantial concern.

2. **Artificial training setup undermines generality.** GOEI is trained on games between two *fixed* strategies (Rand vs. NE), not in interactive online play. The authors explicitly acknowledge this in Section 5: "The effectiveness of the GOEI function in interactive learning should be further confirmed." In real deployment, the strategy and experience distribution co-evolve; this coupling is the central challenge of online model-based RL. By decoupling them, the experiment essentially tests Bayesian model fitting on a fixed data distribution, not the full RL problem. Whether the claimed benefits persist in the online setting remains entirely open.

3. **Scale is extremely limited.** The paper uses a 5-card variant of Hol's der Geier (chosen due to GPU memory constraints with a 12GB card), while the standard game uses 15 cards per suit. No evidence is presented that GOEI scales to the full game or to any other non-trivial domain. The total observation space (15,542 states) is small by modern RL standards, and standard tabular Q-learning is the only baseline—methods designed for large state spaces (e.g., DQN, state abstraction via bisimulation, factored MDPs) are absent.

4. **No comparison with any other state abstraction method.** The paper compares GOEI only against simple fixed strategies (π₀, Rand) and tabular Q-learning. There are established methods for state abstraction in MDPs (Li et al., 2006, which is cited) and modern representational approaches. Without such comparison, it is impossible to assess whether GOEI's state compression is distinctive or whether simpler methods (e.g., hand-crafted feature selection or bisimulation-based aggregation) would perform equivalently.

### Minor

1. **Contradiction in information analysis.** Section 4.2 simultaneously claims that AH and OH are "almost completely reduced" and that they are "likely to be crucial for learning a near-optimal strategy." If those features are nearly eliminated but performance is still near-optimal, the logic requires that the required information is encoded in *combinations* across features—but this is asserted qualitatively without quantitative support. A more careful analysis or a mutual information bound on necessary information for NE play would resolve this.

2. **Hyperparameter selection on the test opponent.** The best hyperparameters (β=0.2, α=25) are selected by directly measuring performance against the NE opponent, which is the test condition. In a setting where NE is unknown (the original motivation of GOEI), this selection procedure would be invalid. The paper does not discuss how hyperparameters would be chosen in practice.

3. **Large sample requirement.** Training uses 300,000 games (200/epoch × 3,000 epochs). For a method motivated by efficient online learning under limited data, no analysis of sample complexity is provided.

### Trivial
None worth noting.

---

## Nice-to-Haves

- Demonstrate GOEI in the interactive online learning regime (joint strategy update + environment inference) to show the method is not limited to the fixed-opponent case.
- Compare against at least one other principled state abstraction baseline (e.g., bisimulation-based or information-theoretic state aggregation) to show that GOEI's compression is not trivially achievable.
- A data efficiency curve (performance vs. number of games, not just epochs) would clarify the sample complexity claim.

---

## Novel Insights

The mutual information breakdown by feature and round (Figure 3) yields a genuinely useful finding: that information about score difference (SD) is nearly irrelevant in early rounds but critical at the final round, while table card identity (CT/RT) matters early. This temporally structured relevance of features is not immediately obvious from game rules and provides a concrete illustration of what "core" information means in this game. Beyond this, the paper's insights align closely with what GOEI is already claimed to do in the prior publication.

---

## Suggestions

- Extend to the interactive learning setting, even on the same 5-card game, as a proof of concept; a negative result here would itself be informative.
- Add at least one state aggregation or bisimulation-based baseline to contextualize the degree of compression GOEI achieves.
- Provide a formal analysis or bound on the minimum state space needed to represent the NE strategy, and compare GOEI's learned compression to this theoretical minimum.

---

## Score and Decision

The paper is technically correct and clearly written, and the NE-anchored evaluation is a clean experimental design. However, it is entirely a validation study of a previously published algorithm (GOEI) applied to one small toy game under an artificial training protocol. The central challenge of online interactive learning is explicitly deferred. No new algorithmic ideas are introduced, and no alternative state abstraction methods are compared. The result—that a good Bayesian state aggregator can compress an observation space while retaining near-optimal performance—is not surprising in principle, and its reach is limited to a 15,542-state game. This contribution is below the bar expected at ICLR for novelty and scope.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>
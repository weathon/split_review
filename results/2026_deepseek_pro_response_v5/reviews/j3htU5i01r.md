Now I have a clear picture from the calibration. Let me finalize the analysis.

**Round 1 bracket**: Paper falls between 4.5-6.5, clearly stronger than the 4.25/4.75 anchors (Olb8JwUGZ3, D1w3huGGpu) but weaker than the 6.50 anchor (H98CVcX1eh, which has theory).

**Round 2 narrowing**: The closest anchors are:
- **6XodKiDS3B (5.50)**: Particle filter + continual learning, has theory + extensive benchmarks (SplitMNIST, CIFAR100, ProcGen). Our paper has no theory and only 2 synthetic tasks — clearly weaker.
- **6r0BOIb771 (5.33)**: Bayesian meta-continual learning, broader evaluation, theoretical grounding. Our paper has narrower evaluation — slightly weaker.
- **3lDxKQepvn (5.75)**: Bayesian meta-learning for simulation, application paper. More domain depth — our paper is weaker.
- **D1w3huGGpu (4.75)**: Modular architecture for embodied agents. Our paper has stronger experiments and more novelty — clearly stronger.

The paper is comparable to or slightly below the 5.33 anchor, placing it around **5.0**.

Now let me write the final review.

---

Here are all anchors across both rounds:

**Round 1:**
- WM5G2NWSYC (2.00): Projected Subnetworks — much weaker, different topic
- ZHTYtXijEn (2.33): Structural adaptation — much weaker
- zEhTnQZB3D (2.33): Continual RL with language — much weaker
- Olb8JwUGZ3 (4.25): When/how modular networks better — our paper clearly stronger (more sophisticated architecture, better experiments)
- 8khcyTc4Di (4.00): Meta-Learning Neural Procedural Biases — different approach, our paper stronger
- Jos5c7vJPP (3.67): Exchangeable Dataset Amortization — different topic
- D1w3huGGpu (4.75): Compositional Interfaces — our paper stronger (better ablations, probabilistic formulation)
- 6r0BOIb771 (5.33): Bayesian continual learning — comparable, our paper slightly weaker (narrower eval)
- VZTFUtldbC (4.75): MeMo modular controllers — our paper stronger
- H98CVcX1eh (6.50): Discovering modular solutions — our paper weaker (no theory)
- unE3TZSAVZ (6.33): Breaking scaling laws with modularity — our paper weaker (theory paper)
- hKMPz3wkPV (6.75): Formal theory of compositionality — our paper weaker
- 3i13Gev2hV (8.00): Compositional VLMs — much stronger, different topic
- zl0HLZOJC9 (8.00): Probabilistic Learning to Defer — much stronger, different topic
- TPZRq4FALB (8.00): Test-time Adaptation — much stronger, different topic

**Round 2:**
- 6XodKiDS3B (5.50): Permutation Invariant Particle Filters — our paper slightly weaker (no theory, narrower eval)
- 3lDxKQepvn (5.75): Latent Task-Specific GNS — our paper slightly weaker
- 5Qxx5KpFms (6.00): Breaking scaling laws with modularity — our paper weaker (theory paper)

Final score: **5.0**, Decision: **Reject**## Final Review

### Summary

This paper proposes a compositional meta-learning framework where a gating RNN selects among a fixed set of module RNNs at each timestep, trained as a probabilistic generative model via particle filtering and marginal likelihood maximization. At test time, solving a new task reduces to inference — finding the module sequence that best explains the task data — without any parameter updates. The method is demonstrated on two synthetic tasks (rule learning and motor learning), where it recovers ground-truth modules and transition statistics, handles sparse feedback through constrained hypothesis testing, and generalizes to tasks four times longer than those seen during training. The paper is explicitly presented as a proof-of-principle.

### Strengths

- **Clean architectural separation validated by recovery experiments**: The architecture isolates within-module computation (module RNNs, Eq. 3-4) from between-module sequencing (gating RNN, Eq. 1-2). Figure 2b,c demonstrates that the module RNNs each learn exactly one ground-truth shift operation while the gating RNN independently captures correct history-dependent transition statistics — recovered simultaneously from a single training objective without supervised labels for either.

- **Probabilistic formulation enables genuine zero-update test-time inference**: By casting the model as a generative model and training via marginal likelihood, new tasks are solved through inference alone. Figure 3e provides compelling evidence: the proposed model solves test tasks from a single episode, while gradient-based methods (MAML, MLDG, pre-trained RNNs) require hundreds of episodes. The magnitude of this gap demonstrates a qualitative difference in sample efficiency.

- **Sparse-feedback inference reveals learned constraints in action**: Figures 2e and 4e show the model's posterior p(z_t|y_{1:t}) remains sharply peaked for the learned module duration in the absence of feedback, then becomes uniform — directly reflecting the gating RNN's learned transition statistics. In the motor task (Figure 4e), the dotted pre-feedback hypotheses branch at skill-switch points and are pruned when feedback returns. This behavior cannot emerge from the flat-transition ablation (Figure 3c), isolating the gating RNN as the necessary component.

- **Systematic ablation design**: Figure 3a-d forms a logical progression: plain RNN fails entirely (3a), adding task ID enables training but not generalization (3b), removing the gating RNN enables one-shot inference but breaks under sparse feedback (3c), only the full model handles all conditions (3d). This decomposition leaves little ambiguity about each component's contribution.

- **Out-of-distribution length generalization**: Figure 2f shows the model infers correct solutions for test tasks four times longer than any training task, with sparse feedback. Gradient-based methods (Figure 3f, green) degrade on doubled-length tasks while the proposed model does not, reinforcing the grammar-learning claim under distribution shift.

- **Cross-domain validation**: The framework is demonstrated on two qualitatively different domains — discrete rule learning (Section 2.2) and continuous motor trajectory generation (Section 2.4) — with principled, domain-appropriate modifications that the authors make explicit rather than hiding.

### Weaknesses

#### Fatal
None.

#### Major
None.

#### Minor

- **Alet et al. (2019) comparison is an untested assertion**: The Discussion (lines 157-160) claims the proposed method "greatly improv[es] sample efficiency" over Alet et al. (2019), which is identified as the most similar prior work. No head-to-head comparison is provided. This claim remains an assertion rather than a demonstrated result, though it appears in the Discussion rather than as a core experimental claim.

- **Evaluation scope matches model assumptions closely**: Both synthetic tasks have structural properties that align with the model's inductive biases: the number of ground-truth operations equals the number of model modules, module durations are fixed and known, and tasks are simple concatenations with no interleaving or hierarchical composition. The paper is transparent about its proof-of-principle scope (line 180: "The results reported here serve as a proof-of-principle"), but the conclusions about compositional meta-learning are necessarily constrained to settings that mirror the model's structure.

- **Smoothing-to-filtering transition not explained in main text**: The paper clearly states that the particle filter provides the filtering distribution p(z_t|y_{1:t}) (line 59), and the heatmaps correctly show this quantity. However, the argmax sequence uses the smoothing posterior p(z_t|y_{1:T}) (line 103, Figure 2d red dots), and the main text does not explain how the smoothing posterior is obtained from the particle filter. This is a standard extension (e.g., forward-filtering backward-sampling) and is presumably detailed in Appendix A.2, but a brief mention in the main text would improve clarity.

#### Trivial

- The particle count K — a key parameter for inference quality and computational cost — is never stated in the main text (deferred to Appendix A.2).

### Nice-to-Haves

- A brief sentence or two in the main text indicating how gradients are handled through the particle filter resampling step (beyond the gumbel-softmax for Eq. 2) would increase confidence in the training procedure, even if full details remain in Appendix A.2.
- Sensitivity analysis for particle count K and discussion of how computational cost scales with task length and module count.
- Experiments under more challenging data-model mismatch (e.g., interleaved rather than concatenated modules, fuzzy module boundaries) to probe the limits of the inference-based approach.
- Training stability data — the paper acknowledges the chicken-and-egg problem (lines 189-192) but provides no data on failure rates or hyperparameter sensitivity.

### Removed Points

These points are flagged to be removed; treat them with caution.

- **Gradient estimation through particle filter underspecified (from Harsh Critic)**: The critic argued this is "structural" and could make training "unsound." However, the loss is computed from pre-resampling likelihoods (Eq. 7-8), which do not directly require differentiating through resampling, and the paper references Appendix A.2 for details. The main text gives the gumbel-softmax strategy for Eq. 2. This is a clarity preference, not a soundness problem — moved to Nice-to-Haves.
- **MAML/MLDG baselines may be undertuned (from Harsh Critic)**: Speculative — no evidence in the paper or reviewer's analysis supports this. The baselines use standard methods with pre-training; the qualitative gap (single episode vs. hundreds) is too large to be explained by tuning differences alone. Removed as speculative.
- **Line 23 phrasing issue (from Harsh Critic)**: "By learning rather than learning new solutions" — this is a minor typo. Removed per hard rule on typos.
- **"The appendix (A.2, stripped) may resolve this" concerns (from Harsh Critic)**: Any weakness whose substance relies on the stripped appendix being absent is removed per the hard rule. The appendix exists in the original submission; its contents are unavailable due to parser stripping, not author omission.

### Novel Insights

None beyond the paper's own contributions. The reviews converge on the same assessment: the core idea of replacing gradient-based meta-learning with probabilistic inference in a modular generative model is coherent and well-executed within its scope, and the sparse-feedback inference behavior (branching/pruning at module boundaries, Figures 2e and 4e) is a genuinely compelling demonstration.

### Suggestions

- Add a direct comparison to Alet et al. (2019) on at least one task, or soften the claim about "greatly improving sample efficiency" in the Discussion.
- Add a brief sentence in the main text (Section 2.1) explaining how the smoothing posterior p(z_t|y_{1:T}) is obtained from the particle filter, even if details remain in the appendix.
- State the particle count K in the main text and briefly discuss its impact on inference quality.

### Calibration Anchors

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| WM5G2NWSYC (Projected Subnetworks) | 2.00 | R1 | Much weaker, different topic |
| ZHTYtXijEn (Directed Structural Adaptation) | 2.33 | R1 | Much weaker |
| zEhTnQZB3D (Continual RL with Language) | 2.33 | R1 | Much weaker |
| Olb8JwUGZ3 (When/how modular networks better) | 4.25 | R1 | Our paper clearly stronger — more sophisticated architecture, better experiments |
| 8khcyTc4Di (Neural Procedural Bias ML) | 4.00 | R1 | Different approach, our paper stronger |
| Jos5c7vJPP (Exchangeable Dataset Amortization) | 3.67 | R1 | Different topic |
| D1w3huGGpu (Compositional Interfaces) | 4.75 | R1 | Our paper stronger — better ablations, probabilistic formulation |
| VZTFUtldbC (MeMo Modular Controllers) | 4.75 | R1 | Our paper stronger |
| **6r0BOIb771 (Bayesian Continual Learning)** | **5.33** | **R1** | **Most comparable; our paper slightly weaker (narrower evaluation, no theory)** |
| 6XodKiDS3B (Permutation Invariant Particle Filters) | 5.50 | R2 | Our paper weaker — has theory + extensive benchmarks |
| 3lDxKQepvn (Latent Task-Specific GNS) | 5.75 | R2 | Our paper slightly weaker |
| 5Qxx5KpFms (Breaking Scaling Laws with Modularity) | 6.00 | R2 | Our paper weaker — theory paper |
| H98CVcX1eh (Discovering Modular Solutions) | 6.50 | R1 | Our paper clearly weaker — has theory + experiments |
| unE3TZSAVZ (Scaling Laws Modularity) | 6.33 | R1 | Our paper weaker |
| hKMPz3wkPV (Formal Theory of Compositionality) | 6.75 | R1 | Our paper clearly weaker |
| 3i13Gev2hV, zl0HLZOJC9, TPZRq4FALB | 8.00 | R1 | Much stronger, different topics |

**Round 1 bracket**: 4.5–6.5. **Round 2**: narrowed to ~5.0–5.5 by comparison with 6XodKiDS3B (5.50, theory + benchmarks) and 6r0BOIb771 (5.33, broader evaluation). The paper is a well-executed proof-of-principle with compelling results but limited evaluation scope and no theoretical contribution, placing it at the lower end of this range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
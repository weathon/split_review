Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces DCWM, a model-based RL method that replaces the continuous latent spaces used in approaches like TD-MPC2 with a discrete codebook encoding via Finite Scalar Quantization (FSQ). The dynamics model is trained as a classifier (cross-entropy loss) over categorical next-code distributions, with Gumbel-Softmax sampling for gradient flow during multi-step rollouts. The method is evaluated on 29 DMControl tasks, 45 Meta-World tasks, and 5 MyoSuite tasks (3 seeds each) against TD-MPC2, DreamerV3, TD-MPC, and SAC. A systematic set of ablations isolates the contributions of discrete vs. continuous latent spaces, classification vs. regression losses, and deterministic vs. stochastic dynamics.

## Strengths

- **Discrete+CE+stoch clearly outperforms continuous alternatives (C1).** Figure 5 (Section 5.2) shows that DCWM's formulation ("Discrete+CE+stoch") achieves higher normalized scores and faster sample efficiency than both "Continuous+MSE" (TD-MPC2-style) and "SimNorm+MSE" on a 10+10 task subset. The gap is consistent across IQM and Optimality Gap metrics.

- **Codebook encoding outperforms one-hot and label encodings (C2).** Figure 6 (Section 5.3) demonstrates that under the same DCWM framework, codebook encoding achieves superior sample efficiency (left panel) and dramatically lower runtime per step (right panel, especially on Humanoid Walk). The paper also provides a clear conceptual explanation for why label encoding fails (it cannot represent multi-dimensional ordinal structure) and why one-hot is computationally expensive.

- **Strong results on high-dimensional locomotion tasks (C3).** Figure 4 (Section 5.1) shows DCWM substantially outperforming both TD-MPC2 and DreamerV3 on the challenging Dog (obs dim 223, action dim 38) and Humanoid (obs dim 67, action dim 24) tasks from DMControl. These are among the hardest continuous control benchmarks, and the advantages are large.

- **Principled ablation design motivates design choices.** Section 3 explicitly contrasts one-hot, label, and codebook encodings on ordinal relationships, sparsity, and dimensionality. The ablation in Figure 5 systematically disentangles the contributions of discrete encoding, classification loss, and stochastic dynamics. The codebook size/latent dimension sensitivity analysis (Figure 10, Section 5.4) shows the method is robust to hyperparameter choices and maintains runtime comparable to TD-MPC2.

## Weaknesses

### Fatal

None.

### Major

- **A confound in the deterministic-vs-stochastic ablation tempers the attribution.** In Figure 5, "Discrete+CE+det" (deterministic dynamics, cross-entropy loss) underperforms "Discrete+CE+stoch" (our method). The paper attributes this to stochasticity (Gumbel-Softmax sampling). However, the two conditions differ in *two* ways: (a) stochastic vs. deterministic dynamics, and (b) how logits are obtained. "Discrete+CE+det" computes logits as the MSE between the dynamics prediction and each code, while "Discrete+CE+stoch" uses a learned MLP classifier that directly outputs logits. A cleaner comparison would hold the logit-computation method constant and only vary whether Gumbel-Softmax sampling is used during training. As it stands, the performance gap could partly stem from the less expressive logit formulation in the deterministic variant, not purely from the presence or absence of stochastic sampling. The additional evidence from continuous stochastic variants (Gaussian, GMM) partially mitigates this concern, but does not fully resolve the confound. (Section 5.2, line 151)

### Minor

- **Abstract overstates the Meta-World result.** The abstract claims DCWM "surpasses recent state-of-the-art algorithms, including TD-MPC2 and DreamerV3, on continuous control benchmarks." On DMControl this is well-supported. On Meta-World, however, the paper's own text (Figure 3 caption, line 89) states DCWM is "generally matching TD-MPC2, whilst significantly outperforming DreamerV3 and SAC." The aggregate plots in Figure 3 (right) show overlapping confidence intervals at 1M steps. The abstract's blanket "surpasses" claim is not accurate for Meta-World. The authors should soften the claim to reflect the matching result on Meta-World. (Abstract, Section 5.1)

- **Evaluation is limited to deterministic environments.** The paper acknowledges in the conclusion (Section 6) that "we have only evaluated DCWM in deterministic environments." All DMControl v2 and Meta-World tasks are deterministic. While this is standard practice for these benchmarks, the paper's central claim—that discrete latent spaces with classification offer benefits for continuous control—is untested under the stochastic transition dynamics that many real-world continuous control problems involve. The paper should either include preliminary results on at least one stochastic benchmark or clearly scope the claim to deterministic environments from the introduction onward, not only in the final limitations paragraph. (Sections 5, 6)

### Trivial

- The paper's caption text in Figure 3 (line 89) correctly states the Meta-World result as "generally matching TD-MPC2," which is more precise than the abstract. Fixing the abstract to match this language would resolve the issue straightforwardly.

## Nice-to-Haves

- An analysis of the learned categorical distributions (e.g., entropy over training, visualization of predicted distributions for specific transitions) would substantiate the claim that the cross-entropy loss captures multimodality and would improve the paper's explanatory power.
- Reporting reward prediction error across tasks would serve as a useful sanity check that the jointly trained reward model (Eq. 8) is accurate enough to support planning.
- Adding a variant where "Discrete+CE+det" still uses a learned classifier (same as the stochastic variant) but without Gumbel-Softmax sampling during training would cleanly resolve the confound discussed above.

## Removed Points

These points were raised by the reviewers but are removed after verification against the paper:

- **"Ordinal relationship phrasing is imprecise"** — the paper states that codebook encodings "preserve ordinal relationships in multiple dimensions" (line 43). The description is sufficiently clear for its purpose and is illustrated with a concrete example. This is a phrasing nitpick.
- **"Expected code at planning time is not rigorously justified"** — the paper explicitly acknowledges this as a heuristic (line 132: "whilst the expected value of a discrete variable does not necessarily take a valid discrete value, we find it effective in our setting"). The paper already addresses the concern.
- **"Fig. 21 results not described in main text"** — referencing an appendix figure is standard practice. The claim is supported by the main-text ablation results and the appendix provides additional confirmation.
- **"Missing related work on discrete-codebook world models"** — I cannot verify the existence or absence of such work; this falls under the rule against raising missing references.
- **"No analysis of learned dynamics / categorical distributions"** — moved to Nice-to-Haves as it is an enhancement, not a flaw.
- **"Reward model accuracy not evaluated"** — moved to Nice-to-Haves.
- **"No confidence intervals on individual task curves"** — this is standard practice in multi-task RL evaluations; aggregate plots with bootstrap CIs are provided.

## Novel Insights

The most novel insight emerging from this review is that the paper's ablation methodology reveals a subtle but common difficulty in empirical RL research: isolating the effect of "stochastic dynamics" requires controlling not just for the presence/absence of sampling, but for how distributional predictions are computed. The "Discrete+CE+det" variant and the "Discrete+CE+stoch" variant differ on two axes simultaneously, making it unclear which axis drives the gap. Future work on discrete latent world models should be mindful of this confound when designing ablations. Beyond this, the paper's own contributions—that codebook encodings with FSQ are more effective than one-hot or label encodings for continuous control world models—stand as the primary novel findings.

## Suggestions

1. **Revise the abstract** to replace "surpasses" with a more precise claim, e.g., "surpasses DreamerV3 and matches or surpasses TD-MPC2 across continuous control benchmarks." This one-sentence fix would resolve the overclaiming issue completely.
2. **Scope the claim to deterministic environments** in the introduction and abstract, not only in the conclusion's limitations paragraph. A phrase like "in deterministic continuous control environments" would be accurate and appropriate.
3. **Add a cleaner ablation** that keeps the logit-computation method fixed (learned MLP classifier) and only varies whether Gumbel-Softmax sampling is used during training, to cleanly isolate the effect of stochastic dynamics from the effect of how logits are produced.
4. **(Optional)** Include results on at least one stochastic continuous control benchmark (e.g., a DMControl variant with stochastic transitions) to broaden the scope of the empirical claims.

## Score and Decision

The paper makes a solid empirical contribution: it demonstrates that a carefully designed discrete codebook latent space with stochastic dynamics and cross-entropy training can outperform continuous latent space methods on challenging continuous control benchmarks. The ablations are systematic and informative. The two substantive weaknesses—a confound in one key ablation and an overstated abstract claim—are addressable and do not invalidate the core findings. The deterministic-only scope is an acknowledged limitation rather than a flaw. Overall, the paper advances understanding of how discrete latent spaces can be effectively used in model-based RL for continuous control.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
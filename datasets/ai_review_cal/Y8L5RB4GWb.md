- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes Reconstruction-Guided Policy (RGP), a method for cooperative multi-agent RL that addresses partial observability by (1) reconstructing an *agent-wise state* (decomposed by agent, rather than by dimension as in prior methods like PTDE and SIDiff) and (2) using this reconstructed state consistently during both training and execution. RGP has a decision module (diffusion-based reconstruction + Q-value prediction) and a guidance module (attention over the global state to produce training targets). Experiments on SMAC, SMACv2, and continuous-action environments show RGP outperforming baselines including PTDE and SIDiff.

## Strengths

1. **Strong empirical performance on standard benchmarks.** In Table 1, RGP achieves the highest mean win rate on 8 out of 10 SMAC/SMACv2 maps (e.g., 95.6% on 2c_vs_64zg vs. 86.4% for the next best SIDiff), and RGP+HPN outperforms HPN-QMIX. The comparison includes a reasonable set of baselines (VDN, QMIX, QPLEX, HPN-QMIX, CADP, PTDE, SIDiff).

2. **Ablation study validates individual components.** Figure 3 breaks down the contribution of each loss term and design choice: removing the Q-value guidance loss (-QLoss) drops win rate from ~90% to ~70% on Protoss 90; the inconsistent-state variant (IState) also degrades performance, confirming that both the guidance module and state consistency are functionally important.

3. **Portability to continuous action environments.** Section 5.6 shows that integrating RGP with MADDPG and FACMAC yields visible improvements in average reward (e.g., from ~1200 to ~1600 in Predator-Prey 6a2p), demonstrating that the core idea transfers beyond discrete action settings.

4. **Robustness under severe partial observability.** Table 3 shows that as the field of view shrinks from 360° to 30°, the gap between RGP/HPN-QMIX and the backbone HPN-QMIX widens (e.g., on Zerg 30: 43.9% vs. 29.5%), suggesting the agent-wise reconstruction is especially valuable when observations are limited.

5. **Clean problem motivation with illustrative example.** The UAV search-and-rescue scenario in Figure 1(a) concretely illustrates why a dimension-wise state can cause agents to overlap rather than cooperate, providing intuitive grounding for the agent-wise representation.

## Weaknesses

### Fatal
None.

### Major

1. **The cross-method PRR comparison (Table 2) is not apples-to-apples, weakening the "consistency" claim.** The paper compares PRR (DE win rate / CE win rate) across methods, asserting RGP's higher PRR demonstrates the benefit of state consistency. However, "centralized execution" means fundamentally different things:
   - **For PTDE/SIDiff:** CE uses the **true global state** — the *same representation* the policy was trained on. The PRR measures the cost of switching from the training-time input to the reconstructed input.
   - **For RGP:** CE uses the **guidance module's output** (derived from the global state via attention). The policy was trained on the *diffusion-reconstructed* agent-wise state, so CE actually feeds a *different* input than training. This could artificially lower CE performance and inflate PRR.
   
   The paper does not acknowledge this asymmetry or justify why the comparison is valid. The better evidence for consistency is the **IState ablation** (within RGP, using guidance output during training and reconstructed state during execution degrades performance), which directly tests the same hypothesis and should be foregrounded instead.

2. **The advantage of agent-wise over dimension-wise representation is not conclusively isolated.** The paper claims that agent-wise states capture inter-agent dependencies better than dimension-wise states. The evidence for this is the overall win-rate comparison against PTDE/SIDiff (Table 1), but superiority could stem from many other factors (diffusion architecture, guidance module, consistency mechanism). The Gstate ablation compares agent-wise against *global* reconstruction, not against *dimension-wise* reconstruction. An ablation within RGP's framework that replaces the agent-wise representation with a dimension-wise one (holding everything else constant) would be needed to directly support this core claim.

### Minor

3. **Figure 4 visualizes guidance module attention, not decision module behavior.** The paper states that Figure 4 shows RGP "effectively captures inter-agent relationships" (RQ4), but the visualized attention weights come from the *guidance module* (which uses multi-head attention on the global state). The *decision module* (used during execution) reconstructs the agent-wise state via diffusion without attention. The paper provides no evidence that the diffusion-reconstructed states actually encode inter-agent relationships in the same way. At minimum, showing that the cosine similarity between reconstructed states of different agents correlates with the guidance module's attention weights would strengthen this claim.

4. **Adaptation to continuous action environments is underspecified.** The paper ports RGP to MADDPG and FACMAC but does not describe how the discrete-action decision module (epsilon-greedy over Q-values from an MLP) is adapted to continuous policies. The text references "Algorithm 2" (presumably in the appendix, which was stripped). The main paper should provide sufficient detail for a reader to judge the soundness of this adaptation.

5. **PTDE and SIDiff are not evaluated in the field-of-view variation experiments (Table 3).** Table 3 only compares RGP against QMIX and HPN-QMIX under varying FOV. Including PTDE and SIDiff would help determine whether the observed trend (larger improvement under narrower FOV) is unique to the agent-wise reconstruction or common to any reconstruction method.

6. **Reconstruction quality is not reported.** The paper does not report reconstruction error (e.g., MSE between the diffusion output and the guidance target) during training. If this error is high, the premise of using the reconstructed state for decision-making is weakened. Reporting this would also help verify whether the diffusion model is performing adequately with only 10 timesteps and an MLP backbone.

7. **Computational cost is not discussed.** The diffusion model requires K=10 iterative denoising steps at every decision timestep, which is an order of magnitude slower than the feed-forward baselines. The paper should acknowledge this trade-off and ideally report inference time or wall-clock runtime.

8. **Loss weighting and hyperparameter sensitivity are not examined.** The total loss (L_l + L_t + L_d + L_g) has at least four terms whose relative weighting could affect performance. The paper does not report how these weights are set or whether performance is sensitive to them.

### Trivial
- Inconsistent use of "dimensional-wise" (abstract) vs. "dimension-wise" (main text).
- "the the state" typo in the Figure 1 caption (line 15).

## Nice-to-Haves
- A dimension-wise ablation within RGP's framework (as discussed in Major weakness 2) would directly isolate the benefit of agent-wise over dimension-wise representation.
- Showing that the guidance module's attention weights correlate with properties of the diffusion-reconstructed states (as discussed in Minor weakness 3) would strengthen the inter-agent relationship claim.
- The paper notes that image-based state representations are a limitation but does not sketch a path forward beyond "object detection or image segmentation." A brief discussion of how agent-wise decomposition might work for visual inputs (e.g., entity-centric representations) would be helpful.

## Removed Points

These points were raised by reviewers but are removed or demoted for the following reasons:

- **"Figure 1(e) would be stronger if it showed RGP's gap."** — Figure 1(e) is an introductory motivation figure showing prior methods only; the actual evidence for RGP is in Table 2 and Figure 3. Demanding RGP data in the motivation figure is scope creep.
- **"Missing related works analysis on why prior methods used dimension-wise states."** — The paper provides a clear motivation for agent-wise vs. dimension-wise; deeper historical analysis is not required.
- **"Guidance targets are not principled (dynamic rather than a fixed decomposition rule)."** — This is a design choice, not a flaw. The method works as designed; the ablation shows the guidance module is functionally important.
- **"Reproducibility concerns about unspecified architecture details."** — The paper specifies MLP diffusion, 10 timesteps, 4 attention heads, Adam optimizer, and references PyMARL2 for tuning. The appendix (stripped from this PDF) would contain the remaining details per community standards.
- **"Statistical significance is not established for win rates."** — The paper reports mean and standard deviation across 3 seeds, which is standard for SMAC experiments. The claim is "best performance in most cases," which is accurate given the reported numbers.
- **"The limitation about image-based states is a significant one."** — The paper already acknowledges this limitation in the conclusion.

## Novel Insights

None beyond the paper's own contributions. The reviews identify important gaps in the evidence chain (PRR comparability, the need for a dimension-wise ablation, the guidance/decision module disconnect in the attention visualization) but do not contribute novel observations about the method or domain.

## Suggestions

1. **Reframe the PRR analysis.** Either (a) make the CE definitions explicit and justify why the cross-method comparison is fair, or (b) remove the cross-method PRR comparison and rely on the IState ablation (within RGP) as the primary evidence for consistency. The IState ablation is cleaner and directly tests your claim.
2. **Add a dimension-wise ablation within RGP's framework.** Replace the agent-wise representation with a dimension-wise one (same dimensionality, but features arranged by dimension rather than by agent) while keeping all other components identical. If agent-wise outperforms, the claim is directly supported.
3. **Clarify what Figure 4 actually shows** — that these are the *guidance module's* attention weights, and that the guidance module's outputs serve as training targets for the diffusion model. Then provide evidence (e.g., similarity analysis) that the diffusion-reconstructed states encode similar relationship information.
4. **Report reconstruction error** between the diffusion outputs and the guidance targets during training to verify the diffusion model is learning meaningful agent-wise states.
5. **Include PTDE and SIDiff in the FOV variation experiments** (Table 3) to show the trend is specific to agent-wise reconstruction.
6. **Expand the continuous-action description** in the main paper and discuss how the architecture differs from the discrete-action case.

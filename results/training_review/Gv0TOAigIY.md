Now I have all the information needed. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

---

Here is the consolidated final review.

---

## Summary

This paper studies how symmetries in neural network loss functions lead to low-capacity states (collapses), and proposes *syre*, a method that adds a static random bias plus weight decay to provably remove reflection symmetries with probability 1 (Theorem 1). The method is architecture-agnostic and requires no knowledge of the underlying symmetries. The paper provides theoretical characterization of symmetry-induced capacity reduction (Propositions 1–2), proves bounds on the strength of symmetry removal (Theorems 3–6), and demonstrates empirical benefits across several settings where collapse is a known problem: VAEs, self-supervised learning, and continual learning.

## Strengths

1. **Clean theoretical guarantee for discrete reflection symmetries (Theorem 1).** The proof that a random bias plus weight decay eliminates all reflection symmetries with probability 1, under mild countability assumptions, is novel and rigorous. The decoupling mechanism between symmetric solutions and weight-decay minima is insightful and clearly explained.

2. **Simple, architecture-agnostic implementation.** The method requires only a static random bias and standard weight decay — one line of code — with no knowledge of the symmetry structure. The compatibility experiments (ResNet-18 on CIFAR-10, linear regression) convincingly show negligible performance degradation for small bias scales (σ₀ < 0.2).

3. **Controlled synthetic benchmark (Section 6.2).** The benchmark directly measures the degree of symmetry against objective value for two spectral types (unstructured and structured). *Syre* is the only method that smoothly interpolates between optimized solutions and low-symmetry solutions, cleanly validating the core controllability claim.

4. **Quantitative characterization of symmetry-breaking strength.** Theorems 3–6 provide lower bounds on gradient asymmetry (scaling with γσ₀) and probabilistic guarantees for multiple symmetries, offering principled guidance for hyperparameter selection.

5. **Broad empirical coverage of collapse-prone scenarios.** The method is tested on posterior collapse in VAEs, last-layer degradation in SimCLR, feature collapse in supervised learning, and loss of plasticity in continual supervised/RL learning — demonstrating relevance across diverse problem settings.

## Weaknesses

### Fatal
None.

### Major

1. **The SSL experiment tests a continuous symmetry with the basic method, contradicting the paper's own theory.** Section 5.2 explicitly states that rotation symmetry yields uncountably many reflection symmetries and that basic *syre* (bias + isotropic weight decay) "is not sufficient to remove all symmetries in this case." Yet the SSL experiment (Section 6.5) attributes the SimCLR last-layer problem to rotation symmetry and applies only the basic *syre* without the diagonal *D* matrix. The paper offers no justification for why the basic method should suffice here, and no measurement of whether the rotation symmetry is actually broken. The claim that "symmetry-induced reduction in model capacity can explain about 50% of the performance difference" is therefore unsupported by the presented evidence — the observed improvement could arise from an entirely different mechanism.

2. **The advanced removal method (ℓ_ar with diagonal *D*, Section 5.2) is never experimentally validated.** The paper devotes a full subsection to the case of uncountably many symmetries (rotation, double rotation), proves Theorem 2, and proposes the ℓ_ar loss with a randomized diagonal *D* matrix. Yet every experiment in the paper sets σ_D = 0 (line 223), reducing ℓ_ar to basic *syre*. No experiment tests the method on a problem with genuine continuous symmetry. This leaves half of the theoretical contribution empirically unsubstantiated — the paper's claimed applicability to rotation and double-rotation symmetries remains unvalidated.

3. **Near-absent statistical rigor across most experiments.** Several figures central to the paper's claims lack error bars, confidence intervals, or any measure of variance:
   - 4-layer FCN (Figure 4): single trajectories, no error bars.
   - VAE rank and reconstruction loss (Figure 6): no variance reported.
   - SSL accuracy (Table 1): no variance reported.
   - Continual learning CNN (Figure 9): single trajectory.
   - Continual RL (Figure 10): "averaged over 5 seeds" but no confidence bounds.
   
   Only the ResNet compatibility experiment (Figure 1 mid) reports standard deviation (10 trials). For a paper that makes quantitative claims (e.g., "50% of the performance difference"), the lack of basic uncertainty quantification undermines the reliability of the experimental conclusions.

### Minor

4. **VAE experiment uses extreme weight decay (γ=1000) without a weight-decay-only baseline.** The VAE experiment compares *syre* at γ=1000 against vanilla at γ=0 (Figure 8). There is no ablation running weight decay alone at γ=1000 (without the bias). Given the extreme γ value, the observed improvement could be partly or entirely due to aggressive regularization forcing a simpler encoder, rather than symmetry removal per se. The RL experiment (Figure 10) does include a weight-decay-only comparison, but the VAE experiment lacks this control.

5. **Assumption 1 (countability of reflection symmetries after subtracting a linear term) is stated but not verified for neural network losses.** The paper claims "this assumption is satisfied by common neural networks with standard activations" (line 122) but provides no proof or characterization. Since the probability-1 guarantee of Theorem 1 depends on this assumption, its unverified status in practical architectures leaves a theoretical gap. The paper would benefit from either proving the assumption holds for common architectures (e.g., ReLU/MLP/CNN) or demonstrating empirically that violating it does not occur in practice.

6. **The SSL improvement is partial and the mechanism is confounded.** Even setting aside the continuous-symmetry issue, Table 1 shows that *syre* improves last-layer accuracy from 22.2% to ~32%, while the penultimate layer achieves 46.8%. The paper acknowledges "symmetry is not the only reason why the last layer representation is defective," but the 50% attribution is a rough estimate with no formal basis. The phrase "can explain about 50%" is not derived from any quantitative decomposition.

### Trivial

7. The probabilistic Ω notation used in Theorems 3–6 is not explicitly defined. The paper defines big-O in probability in a footnote (line 154) but does not define Ω; the meaning is clear from context but should be formalized for precision.

8. The synthetic benchmark (Figure 3) uses scatter plots that make it difficult to judge relative performance across methods. A Pareto-frontier or summary statistic plot would improve interpretability.

## Nice-to-Haves

- A weight-decay-only ablation at matched γ for every experiment (especially the VAE with γ=1000) would disentangle the effect of the bias from pure regularization.
- A toy experiment demonstrating the D-matrix method on a known continuous-symmetry objective (e.g., ℓ(θ) = (‖θ‖² − 1)²) would validate the theoretical extension of Section 5.2.
- Measuring the degree of symmetry actually remaining (e.g., by checking loss invariance under the symmetry transformation) in the SSL and VAE experiments would strengthen the mechanistic claim that *syre* works through symmetry removal.
- Practical guidelines for scaling σ₀ and γ in large models (transformers, LLMs) would increase the paper's immediate utility.

## Removed Points

- **Criticism about missing appendix / proofs in appendix.** The parser strips appendix content from all papers; the original submission contains them. Removed per hard rules.
- **Claim that the paper "never formally defines Ω in probability."** The paper defines the probabilistic big-O (line 154), and Ω in probability follows the same convention. The meaning is unambiguous from context.
- **Criticism that "the proof (presumed in the missing appendix)" is hard to verify.** Parser artifact; the appendix exists in the original submission.
- **Generic complaints about related work coverage (e.g., not discussing noise injection, spectral regularization).** The paper explicitly scopes itself to symmetry-removal methods and cites the most relevant prior work (Lim et al. 2024, Ziyin et al. 2023). Requesting an exhaustive survey of all regularization techniques is scope creep.
- **Complaints that Theorem 3's big-O "is not standard asymptotic analysis."** The paper defines its probabilistic big-O convention (line 154); the usage is appropriate for the probabilistic setting.
- **Strength Finder output listing generic strengths without specific evidence.** Filtered as per instructions; concrete strengths retained.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not already articulate. The core observation — that the paper's SSL experiment contradicts its own theoretical scope — is a weakness noted in the review, not a novel insight about the subject matter.

## Suggestions

1. **Resolve the SSL / rotation-symmetry contradiction.** Either (a) test the D-matrix method on the SimCLR projection head and show it closes more of the gap, or (b) provide a theoretical argument that the specific rotation symmetry in SimCLR decouples into countably many reflection symmetries addressable by basic *syre*, or (c) characterize in what sense basic *syre* can partially break a continuous symmetry and measure what fraction remains.

2. **Add error bars or confidence intervals to all quantitative experiments.** At minimum, report means and standard deviations over ≥5 random seeds for the 4-layer FCN, VAE, SSL, and continual learning experiments. Without this, the reader cannot assess whether effects are systematic.

3. **Test the D-matrix method (ℓ_ar) on at least one controlled continuous-symmetry problem.** A toy rotation-symmetric objective would suffice to validate the theory of Section 5.2 and demonstrate the necessity of σ_D > 0.

4. **Add weight-decay-only baselines matched to the syre γ in the VAE experiment** (and ideally across all experiments) to disentangle regularization from symmetry removal.

5. **Clarify the scope of the SSL claim.** The "50% of the performance difference" attribution should either be derived formally or softened to a qualitative observation, with caveats about the uncertainty introduced by the symmetry-type mismatch.

## Score and Decision

The paper makes a strong theoretical contribution (Theorem 1 and the general-group extension) and proposes a simple, appealingly practical method. The synthetic benchmark provides clean proof-of-concept for controllability. However, the experimental validation has significant gaps: the SSL experiment's mechanism contradicts the paper's own theory, the advanced D-matrix method is never tested, and most quantitative results lack basic statistical rigor. These issues undermine the empirical support for the paper's broader claims but do not invalidate the theoretical contribution.

The paper is a borderline case — the theory is novel and solid, but the experiments need substantial revision (especially resolving the SSL contradiction, testing the D-matrix method, and adding statistical rigor) before the empirical claims can be fully accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
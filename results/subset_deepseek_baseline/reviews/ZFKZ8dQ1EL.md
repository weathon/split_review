## Summary

This paper introduces FedBARRE, a federated learning framework that combines Randomized Ensemble Classifiers (REC) with optimized data perturbations to protect against gradient leakage attacks while minimizing utility loss. The authors prove convexity of the REC adversarial risk, providing theoretical grounding for their approach, and propose a two-tiered framework with server-side aggregation and client-side multi-step adversarial training. Experiments on MNIST, FMNIST, CIFAR-10, and CIFAR-100 show that FedBARRE achieves competitive accuracy while providing stronger privacy protection (higher MSE, lower PSNR/SSIM) compared to DP-based baselines.

## Strengths

- **Novel combination of ensemble methods with perturbation-based privacy**: The idea of using a randomized ensemble classifier with optimized perturbations to balance privacy and utility is creative and addresses a real limitation of existing DP-based approaches that often sacrifice too much accuracy.
- **Theoretical convexity result**: Proving that the REC adversarial risk is convex in perturbations and linear in ensemble weights provides a clean optimization landscape, which is a genuine theoretical contribution that supports the algorithmic design.
- **Comprehensive empirical evaluation**: The paper evaluates on four datasets (MNIST, FMNIST, CIFAR-10, CIFAR-100) with multiple baselines (DP-GAS, DP-LAP, PPFA, Noise-Add) and reports both utility (accuracy) and privacy metrics (MSE, PSNR, SSIM), providing a thorough picture of the privacy-utility trade-off.

## Weaknesses

### Fatal
None.

### Major

1. **The privacy protection mechanism is not well justified theoretically**: The paper claims "provable privacy guarantees" (Section 7) and "rigorous privacy-utility frontier" but never provides a formal privacy definition (like differential privacy, information-theoretic bounds, or reconstruction error bounds). The perturbation set S_priv with norm bounds [ℓ, u] is described as "benign privacy-enforcing noise" but there is no analysis connecting the perturbation magnitude to any concrete privacy guarantee. The convexity result is about optimization tractability, not privacy. This is a significant gap between the claims and what is actually proven.

2. **The experimental setup has serious limitations that undermine the conclusions**: 
   - Only 4 clients are used, which is far from realistic federated learning scenarios (typically hundreds to thousands of clients).
   - Only 30 communication rounds with 1 local epoch per round is very short training.
   - The attack is only evaluated on rounds 9-11 (3 rounds) using DLG, which is a relatively weak attack. Stronger attacks like GradInversion or optimization-based attacks with better priors are not tested.
   - The warm-up period (8 rounds without defense) means the model has already learned useful features before privacy mechanisms kick in, which is an unusual and potentially unrealistic setup.

3. **The privacy metrics are misleading**: Higher MSE and lower PSNR/SSIM indicate worse reconstruction quality, which the paper interprets as better privacy. However, these metrics are highly dependent on the specific attack method used. A different attack might achieve much better reconstruction even with the same defense. Without a formal privacy guarantee, claiming "stronger privacy protection" based solely on attack-dependent metrics is not rigorous.

4. **Missing critical baselines and comparisons**: The paper does not compare against standard DP-FedAvg (with proper ε accounting), Soteria, or other recent defense methods against gradient leakage. The baselines (DP-GAS, DP-LAP, PPFA, Noise-Add) are not well-known or standard in the field. The paper also does not report the actual privacy budget ε used for DP baselines, making it impossible to verify fair comparison.

### Minor

1. **The convexity claim is overstated**: The paper states that G(α, δ) is convex in δ, but this depends on the loss function ℓ being convex in its arguments (which cross-entropy is not for neural networks). The proof in Appendix B likely relies on assumptions that are not satisfied in practice.

2. **The algorithm description is confusing**: Algorithm 2 shows that the gradient g returned to the server is computed on a single mini-batch, but the server aggregates gradients across mini-batches. The relationship between local training epochs and communication rounds is unclear.

3. **The ensemble size experiments (Table 3) show inconsistent trends**: For MNIST, M=1 achieves 92.98% accuracy while M=5 achieves only 90.54%, yet the paper claims "moderate ensemble sizes yield improved utility." The results do not clearly support this conclusion.

### Trivial
None.

## Nice-to-Haves

- Provide a formal privacy guarantee (e.g., differential privacy, mutual information bound, or reconstruction error bound) that connects the perturbation norm constraints to a quantifiable privacy level.
- Test against stronger attacks (e.g., GradInversion with total variation prior, or iterative optimization attacks) to demonstrate robustness.
- Scale experiments to more realistic FL settings (more clients, more rounds, non-IID data distribution).
- Compare against standard DP-FedAvg with proper ε accounting and report the ε values used for all methods.

## Novel Insights

None beyond the paper's own contributions. The convexity of the ensemble risk under perturbations is a useful observation but is a relatively straightforward extension of known properties of convex functions and linear combinations.

## Suggestions

- Remove the claim of "provable privacy guarantees" unless a formal privacy definition is provided and proven. The current paper only proves optimization tractability, not privacy.
- Add experiments with non-IID data distribution, which is the standard setting in federated learning and significantly affects both utility and privacy.
- Report the actual privacy budget ε for DP baselines and ensure fair comparison by using the same ε for all methods.
- Clarify the relationship between the perturbation norm bounds [ℓ, u] and the privacy budget ε—currently they seem to be used interchangeably but are not formally connected.

## Score and Decision

The paper addresses an important problem (privacy-utility trade-off in federated learning) with a novel approach (ensemble + perturbation). However, the lack of formal privacy guarantees, the limited experimental setup (4 clients, short training, weak attacks), and the overclaimed theoretical contributions significantly weaken the paper. The core idea has merit, but in its current form, the evidence does not convincingly demonstrate that FedBARRE provides meaningful privacy protection beyond what simpler methods could achieve.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>
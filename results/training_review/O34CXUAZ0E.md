Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

MARS proposes a backdoor defense for federated learning that uses per-neuron "backdoor energy" (BE), approximated by neuron-wise Lipschitz constants, as a metric supposedly tied to backdoor intent rather than to empirical statistics. The server extracts top-κ% BE values from each layer to form a concentrated backdoor energy (CBE) vector per client, then applies Wasserstein-distance-based K-Means clustering (K-WMeans) to separate backdoor from benign models. Experiments on three datasets against three SOTA attacks and eight defenses show strong empirical performance, including against an adaptive attack, and comparisons with the recent BackdoorIndicator (USENIX 2024) show substantial improvement.

## Strengths

- **Empirically superior to eight SOTA defenses under three advanced attacks**: Across MNIST, CIFAR-10, and CIFAR-100, MARS maintains high CAD while keeping ASR low under MRA, CerP, and 3DFed attacks (Table 2). Against 3DFed — which breaks all other defenses — MARS reportedly maintains CAD above 97% on every dataset, while the next-best defense (FedCLP) suffers a 1.64%–15.82% ACC drop. This is the strongest evidence that the overall approach works.

- **No auxiliary clean dataset required**: Unlike defenses such as BackdoorIndicator that need an OOD/shadow dataset, MARS computes its detection metric from model parameters alone (via the Lipschitz approximation), which is a genuine practical advantage in the federated setting where clean data is unavailable to the server.

- **Thorough evaluation of adaptive attacks**: The paper designs an informed adversary aware of MARS that minimizes BE via regularization, and shows that with a variant (MARS* using majority-based cluster selection) the defense remains effective even when the standard norm-based selection fails (Table 3). This intellectual honesty about failure modes is commendable.

- **Extreme attacker-ratio evaluation**: Experiments explore attacker proportions from 0% to 95% (Table 5), showing 100% TPR and 0% FPR across all settings — this is more thorough than most prior work, which typically assumes attackers are in the minority.

- **Clean theoretical motivation**: The derivation from the BE definition (Eq. 1) through an upper bound (Theorem 1) to the practical Lipschitz approximation (Eq. 3) provides a clear, well-motivated path that explains why clean data and trigger knowledge can be avoided.

## Weaknesses

### Fatal
None.

### Major

- **The core claim that BE (Lipschitz) is "malignity-aware" lacks direct evidence beyond overall system performance.** The paper defines BE conceptually as the expected difference in neuron activations between clean and backdoor-triggered inputs, but the final implementable formula (Eq. 3) drops all terms except the per-neuron Lipschitz constant. The Lipschitz constant measures sensitivity to *any* input perturbation, not specifically to a backdoor trigger. While the upper bound (Eq. 2) provides a theoretical *motivation*, the paper never directly validates that:
  1. neurons in backdoored models have systematically higher Lipschitz constants than those in benign models, or
  2. the specific choice of BE (Lipschitz) is essential rather than incidental.
  An ablation replacing BE with random per-neuron scores (or constant values) would clarify whether any per-neuron variability suffices, or whether the particular Lipschitz-based measure is what drives detection. Without this, the claim that BE is "strongly coupled" with backdoor attacks remains an unverified hypothesis — the empirical success might stem from properties other than the intended "malignity awareness."

- **Missing ablations of key design choices.** (a) The paper advocates for Wasserstein distance over Euclidean/cosine using only a toy example (Table 1); there is no experiment on real CBE data comparing clustering performance across metrics. Since the Wasserstein choice is presented as a core contribution, this absence weakens the claim. (b) Sensitivity analysis of κ (top-κ%) and ε (cluster-distance threshold) is absent — how does performance degrade if κ=1% or 10%, or ε=0.01 or 0.1? (c) The cluster-selection rule (norm-based vs. majority-based) switches heuristically depending on attacker knowledge, but the paper does not characterize how often or under what conditions the norm-based selection would have failed without human intervention.

### Minor

- **The "loose coupling" diagnosis is presented as a key insight but is never formally defined or measured.** The paper describes existing defenses' metrics as "loosely coupled" with backdoor attacks in qualitative terms (Section 4.1 and Figure 2), but does not provide a definition or operationalization that would distinguish "loose" from "tight" coupling. This weakens the claim to a post-hoc observation rather than a falsifiable thesis.

- **The CAD metric is not formally defined in the main text.** The paper lists CAD among evaluation metrics (line 191) and uses it to compare methods, but never states its formula. This makes it difficult for readers to interpret the reported numbers precisely.

- **The adaptive-attack analysis leaves an important scenario unexplored.** The paper shows that when attackers constrain BE (λ ≥ 0.05), norm-based selection fails and MARS* (majority-based) rescues the defense. However, in scenarios where attackers are *both* a majority *and* constrain BE, both selection strategies would fail simultaneously. This case is neither discussed nor tested, and the attacker-model assumption (Section 3.1) explicitly allows attackers to be a majority.

### Trivial
- The paper notes that "7 examines MARS's effectiveness on larger datasets such as ImageNet" (line 227). This section appears to have been in the (stripped) appendix, so it is not viewable in the current form.

## Nice-to-Haves

- Provide histograms or PCA visualizations of BE distributions for benign vs. backdoored models (e.g., on CIFAR-10 under 3DFed) to directly test whether BE separates the two populations.
- Report wall-clock time per round for MARS compared to FedAvg and other defenses, since computing Lipschitz constants for every neuron each round incurs non-trivial overhead.
- Discuss whether baselines (Multi-Krum, FLAME, etc.) had their sensitive hyperparameters tuned for each attack/dataset, as unequal tuning can skew comparisons.

## Removed Points

These points were flagged by the reviewers but are removed per the stated rules. Treat them with caution — they are not valid criticisms of the paper.

1. **"The proof of Theorem 1 is not included (appendix stripped)."** — Parser artifact. The appendix exists in the original submission.
2. **"Table 2 numbers are not available (only placeholder images)."** — Parser artifact. The images with numerical data exist in the original submission.
3. **"The BE definition (Eq. 1) requires clean data, contradicting the threat model."** — The paper explicitly acknowledges this challenge (lines 124–125) and derives an approximation that avoids the requirement. The paper addresses this concern.
4. **"No mention of defenses using neuron-level analysis (e.g., clipping per-neuron contributions)."** — Missing-related-work criticism. Per instructions, this is removed as the reviewer cannot verify existence of unmentioned works.
5. **"The Wasserstein distance on sorted CBE vectors is essentially L1 distance."** — This is inaccurate: the paper's CBE vectors are constructed as sorted within each layer then concatenated, but Wasserstein distance on these 1D sorted vectors is not equivalent to L1; it computes the optimal transport cost between the empirical distributions, which *is* the L1 distance between sorted vectors *only* when both vectors have the same length. The paper's claim that Wasserstein is less sensitive to element ordering is well-motivated for the described scenario.
6. **"Strength about principled/attack-coupled metric" from Strength Finder** — This strength is kept in the main review (see Strengths section) rather than removed, but the Weaknesses section clarifies that the empirical support for the "attack-coupled" claim is incomplete.
7. **"The paper does not formally define 'loose coupling' or measure it"** — This was moved to Minor (not removed), as it is a fair observation but not a fatal flaw.
8. **The harsh critic's Section‑by‑Section note about "the defense model assumes the server has no access to any client's training data — but MARS's original BE definition (Eq. 1) requires a clean dataset"** — Already addressed by the paper; the whole point of Theorem 1 and Eq. 3 is to circumvent this requirement.

## Novel Insights

A genuinely novel observation that emerges from considering the reviews together is that MARS's strength may lie less in the specific Lipschitz-based BE metric than in the *concentration* and *distributional* approach: extracting top-κ% values per layer and then comparing their distributions via Wasserstein distance. The toy example and the strong empirical results suggest that even if the theoretical "malignity-awareness" claim were overstated, the pipeline of (1) focusing on extreme activation values per layer and (2) comparing their distributions rather than their ordered vectors could be a generally useful detection principle. This reframing — that the method's robustness may derive from the distributional comparison of extreme values rather than from a theoretically grounded backdoor-energy measure — is a more honest and testable hypothesis than the paper's current framing, and would strengthen rather than weaken the contribution if validated with the recommended ablations.

## Suggestions

1. **Add a direct BE validation experiment.** Provide histograms or violin plots of neuron-wise Lipschitz constants (BE) for benign vs. backdoored models on at least one dataset/attack (e.g., CIFAR-10 under 3DFed). If BE distributions overlap substantially, the paper should reframe the contribution more modestly as an empirically effective defense rather than a theoretically "malignity-aware" one.
2. **Add an ablation replacing BE with random per-neuron scores.** If MARS still works with random scores, the core claim is unsupported and the contribution should be reframed accordingly.
3. **Add an ablation comparing Wasserstein vs. Euclidean/cosine distance on real CBE data.** Report TPR/FPR under 3DFed for each metric to substantiate the claimed advantage.
4. **Define the CAD metric explicitly** in the next revision.
5. **Discuss and ideally test the scenario** where attackers are a majority *and* constrain BE (λ ≥ 0.05), since both selection strategies would be challenged in this case.
6. **Reduce emphasis on "malignity-aware" as a theoretical property of BE** and instead present the approach as an empirically motivated and well-performing defense. The paper's results are strong enough to stand on their own without overclaiming the theoretical grounding.

## Score and Decision

The paper addresses an important problem and presents a defense that, by the reported results, substantially outperforms existing methods across a wide range of attacks and settings. The core concern is that the paper overclaims the theoretical grounding of its detection metric ("malignity-aware") without direct validation that BE (Lipschitz) specifically captures backdoor intent rather than other properties. However, the empirical results are extensive and convincing enough to support the claim that MARS is an effective defense, even if the explanation for *why* it works may need refinement. The missing ablations are addressable in revision. The paper represents a meaningful advance over prior defenses, particularly against 3DFed attacks that break all compared baselines.

Given the strong empirical evaluation but the need for better validation of the metric at the heart of the claimed novelty, the appropriate assessment is a **weak accept** contingent on addressing the major weaknesses in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
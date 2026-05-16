Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper studies how sharing a single source network across multiple target models (ensembles, MoEs) can reduce memory in Strong Lottery Ticket (SLT) constructions. The authors prove that sharing a source does not increase the width requirement beyond a log factor compared to separate sources, identify that independently optimizing each mask for sparsity is suboptimal for joint memory, and propose several mask selection algorithms (Partition, Local-bin, Local-bin+opt) along with an (m+1) storage scheme that decomposes masks into shared overlap and individual planes. Experiments on synthetic subset-sum approximation problems (n ≤ 17, m = 4) show that Local-bin+opt with a shared source reduces total bits compared to baseline selection methods.

## Strengths

- **Theoretical proof that sharing a source avoids width overhead for model families (Theorem 3.3).** The paper correctly extends the Pensia et al. SLT construction to show that a shared source requires width ~ C d log(1/δ) while m separate sources require ~ C d log(m/δ). This formalizes a non-obvious advantage of source sharing and connects it to existing SLT theory.

- **Identification that individual mask sparsity optimization is suboptimal for joint memory (Theorem 3.5).** While the inequality itself is a simple union bound, the insight that minimizing each mask independently is only an upper bound on minimizing the union of masks motivates the paper's joint optimization approach and is a valid observation about subset-sum approximation.

- **The (m+1) storage scheme and Local-bin+opt algorithm.** The decomposition of masks into an overlap plane plus m extra planes provides a concrete encoding that can exploit mask overlap. The Local-bin+opt algorithm that minimizes total length (overlap + extra bits) is a principled approach, and the experiments confirm it reduces total bits compared to independent sparsity optimization under this scheme.

- **Experimental evidence that shared sources increase mask overlap.** Figure 1 shows that under joint optimization (Local-bin+opt), using a shared source yields higher overlap and lower extra bits than different sources, confirming the theoretical intuition about shared sources enabling more memory-efficient representations.

## Weaknesses

### Fatal
None.

### Major

- **Abstract overclaims about experimental validation.** The abstract states "To validate these theoretical findings, we provide explicit SLT constructions in experiments." The experiments contain no actual neural network SLT constructions — they only simulate subset-sum approximation on synthetic data (n ≤ 17, m = 4). While the theoretical connection between subset-sum approximation and SLTs is already established by Pensia et al., claiming "explicit SLT constructions in experiments" is misleading and sets false expectations. This should be corrected to accurately describe what is validated (subset-sum approximation algorithms, not end-to-end neural network lottery tickets).

- **Theorem 3.4's justification of the mask overlap probability is incomplete.** The theorem claims that with reshuffled (separate) sources, the probability of perfect index-level overlap between M¹ and M² is 1/C(n,k). The proof simply states "This follows from the probability of permutations" and describes drawing k-subsets without replacement. This calculation would be correct for uniformly random k-subsets, but the masks are not uniformly random — they are determined by the subset-sum approximation problem, which depends on the specific values in the source sets. No argument is given that the distribution of approximation solutions is uniform. The first part of the theorem (same source → M¹ = M² when the same z approximates both targets) is straightforward and correct, but the probability claim lacks a rigorous justification. This weakens the theoretical argument for why shared sources are advantageous for mask overlap.

### Minor

- **Experiments are limited to very small source sizes (n ≤ 17) and do not demonstrate scaling.** The experiments use exhaustive enumeration over 2ⁿ possibilities, which is only feasible because n is tiny. For n=17, 2ⁿ=131,072; for real neural network settings (n could be much larger), this approach is intractable. The Discussion acknowledges this exponential complexity, but the paper does not provide any heuristic or approximation strategy for larger n, nor does it show results beyond n=17. A reader cannot assess whether the approach has practical relevance for the large models cited in the introduction.

- **Experiments test average-case behavior with randomly sampled X each iteration, not a fixed source.** The 10,000 iterations each resample both the source set X and the target vector Z (line 157). This tests average-case behavior but does not directly validate that the optimized masks work for a single fixed random source — which is the scenario most relevant to actual SLT deployment where a source network is fixed and targets are approximated from it. Some analysis with a fixed source would strengthen the connection to the claimed application.

- **No comparison to simple baselines outside the proposed method family.** The paper compares Partition, Local-bin, and Local-bin+opt against each other. There is no comparison to a baseline such as "store masks without any optimization" (e.g., random mask selection or storing the full target weights) or standard sparse encoding methods. This makes it difficult to contextualize the claimed memory savings.

### Trivial
- Theorem 3.4's statement contains a formatting artifact ("$z_{1}$ $\mathrm{i},z_{2}$") in the extracted text.
- Section 3 would benefit from a clearer distinction between what is existing result (Theorem 3.1 from Pensia et al.) and what is novel (Theorems 3.3–3.5).

## Nice-to-Haves
- A heuristic or approximate (e.g., greedy) variant of Local-bin+opt that works for larger n (e.g., n=100) would substantially strengthen the practical claims. The paper acknowledges exponential complexity but provides no path forward.
- A concrete example of how the framework applies to a small MLP (e.g., a 3-layer network with width 50), even just theoretically tracing the parameter counts, would help bridge the gap between the subset-sum abstraction and the neural network claims.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic's claim that "The paper never verifies that the masks found by its proposed algorithms actually yield functional lottery tickets"** — The connection between subset-sum approximation and SLT construction is already proven by Pensia et al.; the paper's algorithms only select masks that satisfy the approximation bound, so the construction is valid by existing theoretical results. Verifying subset-sum approximation is sufficient for the theoretical claim.

2. **Harsh critic's demand for "neural-network experiment" (MLP layer test) as a requirement for acceptance** — This paper is primarily theoretical; its experiments validate the subset-sum algorithms which are the building blocks of the SLT construction. Evaluating against standards for an empirical systems paper is inappropriate for a theory+methodology paper.

3. **Harsh critic's complaint about "no measurement of actual compression ratios, no comparison with standard encoding schemes (run-length encoding, compressed sparse row)"** — These are demands for a broader empirical study that would change the paper's nature. The paper proposes and evaluates a specific framework (mask overlap optimization + (m+1) scheme) and compares different selection strategies within that framework. Adding standard compression baselines could enrich the paper but their absence is not a structural flaw.

4. **Harsh critic's claim that "Theorem 3.2 is a standard union bound and Theorem 3.3 is a direct corollary" — "correct but not novel"** — Novelty is not required for every theorem; applying existing techniques to establish a new result (shared source doesn't increase width) is a valid contribution. Papers routinely extend prior proofs.

5. **Harsh critic's criticism about overlapping masks not being verified for neural network approximation error** — The algorithm only selects subsets that satisfy the per-parameter approximation guarantee |subsetSum - target| < ε. Since SLT constructions decompose to independent parameter-level subset-sum approximations (per Pensia et al.), the joint optimization does not affect the approximation error guarantee for any individual parameter.

6. **Harsh critic's criticism about "inference speed" not being measured** — The paper uses set bits as a proxy for computations (which it states), and measuring actual inference speed on a fabricated neural network is outside the scope of a paper whose experimental focus is subset-sum approximation.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the multiple valid subset-sum solutions for each target can be jointly selected to maximize overlap and reduce memory — is the paper's own novel observation, and the reviewer analyses do not add substantially to it beyond identifying that the experimental validation of this insight on neural networks is incomplete.

## Suggestions

1. **Correct the abstract and framing.** Replace "we provide explicit SLT constructions in experiments" with an accurate description of what is validated (e.g., "we validate the subset-sum approximation component of SLT constructions with synthetic experiments").
2. **Fix the proof of Theorem 3.4** by either (a) providing a rigorous justification for the 1/C(n,k) probability, (b) explicitly stating the uniformity assumption, or (c) removing the probability claim and keeping only the qualitative statement that overlap is unlikely with separate sources.
3. **Add at least one experiment with a fixed source set** (not resampled each iteration) to match the SLT deployment scenario.
4. **Include a concrete estimate** translating the n=17, m=4 bit savings to approximate parameter counts for a small neural network (e.g., an MLP with the architecture from Theorem 3.3) to help readers understand the practical implications.
5. **Discuss or propose a way forward for larger n** — even a simple greedy heuristic or random sampling approach would address the scalability concern.

## Score and Decision

**Originality:** Moderate. The core observation (joint mask selection can reduce memory) is novel, though several theoretical building blocks adapt existing results.  
**Importance of research question:** High. Memory-efficient representation of model families is a practically relevant problem.  
**Claims well supported?** Partially. The theoretical claims are sound (except Theorem 3.4's probability claim), but the experiments are too small-scale to support the large-model framing.  
**Soundness of experiments:** Adequate for a theory paper but limited in scope and scale.  
**Clarity of writing:** Generally clear, though the abstract overstates what is experimentally demonstrated.  
**Value to the community:** Moderate. The theoretical insights about joint mask optimization could inform future SLT-based compression work, but the lack of scaling analysis limits near-term impact.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
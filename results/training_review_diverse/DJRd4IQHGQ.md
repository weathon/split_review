Now I have everything I need. Let me write the consolidated review.

## Summary

FeedSign proposes a federated fine-tuning algorithm that reduces per-step client-server communication to exactly 1 bit (a binary vote on whether a random perturbation direction reduces the loss), achieved by combining zeroth-order optimization with shared pseudo-random number generators across devices. The paper provides a convergence analysis (exponential rate 𝒪(e^{-t})), demonstrates scalability across models from 11M to 13B parameters, and shows strong empirical robustness to data heterogeneity and Byzantine attacks. Despite the extreme compression, FeedSign achieves performance within a few percent of far more communication-expensive baselines.

## Strengths

- **Extremely low communication overhead (1 bit per step, scale-invariant)**: The paper demonstrates that each client uploads exactly 1 bit per communication round regardless of model size, reducing communication from ~100 MB (FedAvg on RoBERTa-large) to 1 bit. This is verified by experiments on models up to OPT-13B (1 bit vs. 24 GB per step).

- **Empirical robustness to data heterogeneity**: Under non-iid (Dirichlet-based) data splits, FeedSign consistently outperforms ZO-FedSGD across multiple language tasks (e.g., +3.6% on SST-2, +4.0% on RTE), confirming the theoretically implied heterogeneity robustness.

- **Byzantine attack resilience**: With one Byzantine client sending reversed signs (the worst possible attack on a binary system), FeedSign maintains high accuracy (e.g., 81.8% on MNLI) while ZO-FedSGD drops sharply (48.3% on QNLI). On ViT-large, ZO-FedSGD is "completely compromised" while FeedSign maintains performance.

- **Scalability to large models**: Experiments on OPT-13B (Table 2) show a mean gap of only –6.0% compared to full-parameter FO fine-tuning, with 1 bit vs. 24 GB per step, demonstrating the method works at 13-billion-parameter scale.

- **Inference-level memory demand**: The ZO-based design squeezes memory to the amount needed for inference (roughly 1/12 for transformer-based models), enabling deployment on consumer devices.

- **Practical byproducts via minimalistic design**: The orbit-based model storage (less than 200 bytes for 10 k steps vs. 24 GB), parameter-server security (PS does not hold actual model weights), and a differentially private variant (Theorem 2) are concrete advantages that arise naturally from the 1-bit framework (Section 5).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Downlink communication claim needs clarification**: The paper states that clients "download the global model … using exactly 1 bit per step" (abstract) and "download one bit" (conclusion), but the method also relies on a random seed being agreed upon between the PS and clients. The paper mentions "shared PRNG across devices" which is standard in this line of work (FwdLLM, FedKSeed), and the seed can be derived deterministically from the step count — but the paper never makes this explicit. The actual downlink is indeed 1 bit (the aggregated vote) if the seed is implicitly agreed upon, but the text should state this clearly rather than leaving readers to infer it.

- **Convergence rate claim lacks stated assumptions in the main visible text**: The abstract and introduction state that FeedSign "converges at an exponential rate 𝒪(e^{-t})" and claim this "matches first-order methods in big 𝒪 notation." First-order methods achieve linear/exponential convergence only under strong convexity or the Polyak-Łojasiewicz condition; for general non-convex objectives they obtain sublinear rates. The paper's Section 3 (Method and Theory) was stripped by the parser, so the full assumptions may be stated there — but the abstract and introduction should at least reference the required conditions (e.g., "under the PL condition") to avoid misleading readers who skim the front matter.

- **No variance/error bars reported for any experiment**: The paper does not report standard deviations, confidence intervals, or results from multiple random seeds for any of its experiments. Given that FeedSign uses a single random perturbation per step and 1-bit feedback, results could be noisy across runs. This is especially important for the iid vs. non-iid comparisons (Tables 3–5) where the reported gaps are often small (a few percent). Reporting variance across at least 3–5 trials would substantially strengthen confidence in the conclusions.

- **ZO-FedSGD baseline is referenced but not described**: The paper assumes reader familiarity with Xu et al. (2024) and Qin et al. (2023). A brief description of how ZO-FedSGD operates (how it communicates projection-seed pairs, its per-step communication cost in KB) would help readers judge whether it is a strong contemporary competitor.

- **"Total perturbations" claim is ambiguous**: The paper states "We kept the number of total perturbations consistent with that adopted in MeZO. As a result, the number of elapsed steps of MeZO is K times that of ZO-FedSGD and FeedSign." It is unclear whether "total perturbations" refers to the sum over all clients and steps or the per-step per-client count, which affects the fairness interpretation.

### Trivial

- In the conclusion, "each client needs only to upload one bit to the PS and then download one bit as a global update direction metric in a step" — the phrase "metric" seems to be a small typo (likely "in a step" or "per step"); this does not affect understanding.

## Nice-to-Haves

- An ablation on the number of random directions per step: using multiple perturbations per round (e.g., m random seeds, each with a binary vote) would illuminate the trade-off between communication and convergence speed.
- A brief discussion positioning FeedSign relative to gradient compression techniques (SignSGD, Top-k, QSGD) in the federated setting would help contextualize the communication savings.
- An approximate FLOPs comparison between FeedSign (two forward passes per client per step) and FO fine-tuning (forward + backward) would complete the resource picture.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Byzantine attack asymmetry (unfair comparison)**: Removed per hard rules. The reversed sign is the worst possible attack on a binary system (always the opposite direction), while a random number may not be the worst attack on ZO-FedSGD (gradient ascent with large magnitude would be stronger). The asymmetry thus favors the baseline, not the author's method. The reviewer's suggestion that "random signs" would be a stronger test for FeedSign is factually incorrect — reversed sign is strictly stronger.

- **Tables replaced with images**: Removed as a parser artifact. The original submission contains proper tables.

- **Missing appendix/proofs to verify theory**: Removed per hard rules. Section 3 (Method + Theory) and the appendix were stripped by the parser; they exist in the original submission.

- **Missing related works (SignSGD, Top-k, QSGD)**: Removed per hard rules — the reviewer cannot confirm these are missing from the paper's related work section.

- **Formatting/style nitpicks**: Removed per hard rules.

## Novel Insights

The key insight that emerges from the reviews — beyond the paper's own contributions — is that FeedSign's design creates an unusual situation where the method's most extreme compression (1 bit) is also its strongest asset for robustness. The binary nature of the vote means that Byzantine attacks can do no more than flip a single bit (the worst case is reversed sign, which is already tested), and data heterogeneity is naturally mitigated because each client only reports a directional vote rather than a precise gradient magnitude. This "strength through minimalism" narrative is present in the paper but could be foregrounded more explicitly as the unifying story. The orbit-based storage byproduct (Sections 5.1–5.2) is also a genuinely interesting idea that goes beyond typical FL efficiency arguments and suggests a different model-sharing ecosystem.

## Suggestions

1. **Clarify the seed agreement mechanism explicitly**: Add one sentence in Section 3 stating that "the seed for each round is derived from the step count (or broadcast once at setup), so the PS only transmits the 1-bit aggregated vote per round."
2. **Add a brief statement of convergence assumptions in the introduction or at the start of the theory section**: e.g., "Under standard assumptions (PL condition, L-smoothness, bounded variance; see Assumption 1), FeedSign achieves an exponential convergence rate 𝒪(e^{-t}) in the federated setting."
3. **Report variance across at least 3 random seeds for the main experimental tables** (Tables 1–7), or at minimum for the heterogeneity and Byzantine experiments where the claims depend on relative ordering.
4. **Provide a 2–3 sentence description of ZO-FedSGD** when it is first introduced as a baseline, explaining its communication pattern (seed + projection value per step) so readers can understand why FeedSign is 64× cheaper.

## Score and Decision

This paper proposes a genuinely novel and well-executed approach to federated fine-tuning that pushes communication compression to its theoretical minimum (1 bit per step) while preserving competitive performance, theoretical convergence guarantees, and practical robustness. The experiments span models from 11M to 13B parameters, which is unusually thorough. The weaknesses identified (imprecise downlink description, unstated convergence assumptions in the main text, lack of variance reporting) are all addressable and do not threaten the core contribution. The paper would be a strong addition to the federated learning and efficient fine-tuning literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
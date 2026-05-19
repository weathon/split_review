- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6
Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated final review.

---

## Summary

FeedSign proposes a federated fine-tuning framework that leverages zeroth-order (ZO) optimization with shared pseudo-random number generators (PRNGs) to reduce per-step client-to-server communication to exactly one bit (a binary vote on the loss descent direction), while maintaining inference-level memory requirements. The method is evaluated across models spanning 11M to 13B parameters (ResNet, ViT, RoBERTa, OPT) on language and vision tasks, achieving test performance within −5.5% to −6.0% of first-order methods while using orders-of-magnitude less communication. The paper also provides a convergence analysis (Section 3, missing from parsed text) claiming exponential rate O(e⁻ᵗ), and discusses robustness to data heterogeneity and Byzantine attacks, along with byproducts such as orbit-based model storage.

## Strengths

- **Extreme communication reduction to 1 bit per step regardless of model size**: FeedSign achieves per-step uplink communication of exactly 1 bit by combining ZO optimization with shared PRNGs, so each client sends only a binary vote. This is a genuine advance over prior seed-projection pair methods (FwdLLM, FedKSeed) which still required KB-level overhead. The logarithmic-scale comparison in Figure 1 (right) illustrates the magnitude of reduction relative to FedAvg and ZO baselines.

- **Competitive empirical performance across diverse models (11M–13B parameters) and tasks**: Tables 1–4 show that FeedSign's test metrics fall within a mean gap of −5.5% to −6.0% compared to first-order methods for RoBERTa-large and OPT-13B across language tasks, and reaches 91.7% accuracy on ViT-large/CIFAR-10, all while using 1/64 the communication of ZO-FedSGD and orders-of-magnitude less than FO methods. This scaling across both vision and language architectures, including the largest tested model (OPT-13B), demonstrates the method's generality.

- **Demonstrated robustness advantages over ZO-FedSGD under data heterogeneity and Byzantine attacks**: Table 5 (language tasks with β=0.5 Dirichlet non-iid splits) and Figure 2 (vision models) show FeedSign outperforming ZO-FedSGD under data heterogeneity. Tables 6–7 and Figure 3 establish that FeedSign maintains performance under a Byzantine attack (reversed sign) while ZO-FedSGD collapses to near-chance accuracy in the vision case. These results are limited in scope but clearly favor FeedSign.

- **Novel byproducts with practical value**: The orbit-based model storage proposal (Section 5.1) — storing a fine-tuned OPT-13B model as <200 bytes of seed-projection pairs versus 24 GB — is a creative and concrete advantage. The implication that the parameter server need not hold model parameters (Section 5.2) and the DP mechanism (Section 5.3) are interesting extensions beyond the core communication contribution.

- **Inference-level memory demand**: As a consequence of ZO optimization (no backpropagation), FeedSign requires memory roughly equal to inference (~1/12 of FO memory for transformers per Malladi et al. 2023), which is a practical advantage for deployment on resource-constrained devices.

## Weaknesses

### Fatal
None. The core idea is sound and the 1-bit claim is technically correct under the shared-PRNG mechanism; no criticism from the reviews, when verified against the paper, rises to the level of invalidating the paper's central claims.

### Major

- **The convergence analysis is unverifiable from the supplied material, and the stated O(e⁻ᵗ) rate matching first-order methods is a very strong claim for ZO sign-based methods on non-convex objectives.** Section 3 (method description and convergence analysis) is missing from the parsed text, so the assumptions behind Theorem 1 cannot be checked. Even in the paper's full form, claiming exponential convergence for ZO sign-based optimization on non-convex large-scale deep learning models (ResNet, ViT, OPT-13B) would require unusually strong conditions (e.g., gradient dominance / PL structure, or sign agreement assumptions) that are unlikely to hold in these settings. The paper does not qualify this claim with respect to the non-convexity of real models. The authors should explicitly state what assumptions Theorem 1 requires and discuss whether they hold in practice.

- **The evidence for robustness claims is too narrow to support their strength.** The paper makes general claims about "good robustness against data heterogeneity and Byzantine attacks" (abstract) and "surprising effects addressing… data heterogeneity, and Byzantine vulnerability" (Section 1), but the empirical support is limited to a single data heterogeneity level (β=0.5, one value) and a single attack scenario (1 out of 5 Byzantine clients sending reversed signs). There are no error bars, confidence intervals, or variance reports across random seeds. Without varying the severity of heterogeneity, the fraction and type of Byzantine clients, or reporting statistical significance, the robustness conclusions are suggestive but not conclusive.

- **The 1-bit communication claim is stated imprecisely across the paper.** The abstract says clients "upload its update model and download the global model of any size using exactly 1 bit per step," which conflates the model parameters themselves with the binary vote. The contribution list (point 1) correctly states "per-step uplink communication overhead of 1 bit," but the conclusion reasserts "upload one bit … and then download one bit." This inconsistency in wording creates unnecessary confusion about what exactly is communicated. The claim itself is correct (with shared PRNGs, the perturbation direction is determined deterministically and does not require per-step seed broadcast), but it should be stated cleanly and consistently: each client sends a single sign bit, and the PS replies with a single aggregated sign bit.

### Minor

- **Experimental reproducibility details are incomplete.** The parsed text does not specify the learning rate, local steps per round, batch size, or learning rate schedule used in the experiments. The perturbation count is stated as "consistent with MeZO" but not listed explicitly. These details are necessary for reproducibility and should be provided.

- **The comparison to ZO-FedSGD only accounts for total perturbation count but does not control for other hyperparameter tuning.** The paper states "the number of total perturbations consistent with that adopted in MeZO" but does not confirm that ZO-FedSGD's learning rate and other settings were individually optimized. An unfair baseline would undermine the robustness comparisons.

- **No comparison to existing gradient compression techniques (signSGD, QSGD, Top-k sparsification).** While the paper correctly identifies ZO-based FL works (FwdLLM, FedKSeed) as the closest prior art, the FL compression literature includes signSGD and variants that also achieve aggressive compression. A brief discussion of why FeedSign's approach is preferable in the large-model fine-tuning setting would strengthen the contextual positioning.

### Trivial

- The parsed text contains several garbled passages (e.g., "vithth del faster tha" on line 67) and inconsistent table parsing — these are parser artifacts, not author errors, but the original submission should be checked for clarity.
- The paper uses "zeroth-order" and "ZO" interchangeably but could define the acronym more prominently.

## Nice-to-Haves

- Report error bars or confidence intervals for key experimental results, especially the robustness experiments.
- Vary the fraction of Byzantine clients and test additional attack strategies (e.g., Gaussian noise, sign flipping by a majority of clients).
- Test multiple Dirichlet β values (e.g., 0.1, 0.3, 0.5, 1.0) to demonstrate robustness across heterogeneity levels.
- Provide a clear pseudocode or algorithm box for the basic FeedSign protocol (Algorithm 1 is referenced but its content is missing from the parsed text).
- Include convergence curves (loss vs. steps) for all main experiments, not just vision models (Figure 2).

## Removed Points

*These points are flagged to be removed. Treat them with caution; they may represent reviewer misunderstanding or parser artifacts.*

- **"The 1-bit claim is unsupported and likely misrepresented — seed must be broadcast"** (Harsh Critic #1): The reviewer assumes the PS broadcasts a seed per step, but the paper's core mechanism uses *shared PRNGs* initialized once, allowing all parties to deterministically generate the same perturbation directions without per-step seed communication. The 1-bit claim is technically sound. Removed because the criticism misunderstands the shared-PRNG mechanism.

- **"Convergence analysis is entirely absent"** (Harsh Critic #2): Section 3 is missing due to parser stripping, not author omission. The existing paper contained a full Section 3 with Theorem 1 and convergence analysis. The substantive concern about plausibility is retained in Major weakness #1 above, but the claim that it's "absent" is a parser artifact.

- **"The downlink protocol is unclear"** (Harsh Critic, Section-by-Section): The conclusion states "download one bit as a global update direction metric in a step." The PS broadcasts the aggregated sign (1 bit). This is clear from the conclusion. Removed as the concern is addressed.

- **"Missing related works"** (Harsh Critic): The instructions forbid mentioning missing related works as I cannot independently verify their existence. Removed.

- **Strengths removed from Strength Finder**: The claimed strength about "theoretical convergence rate matching first-order methods" is demoted because Theorem 1 cannot be verified from the available text. The generic/phrasing-based strengths (e.g., "addressed an important problem") are removed per instructions.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews with the paper is the tension between the paper's bold framing and the actual precision of its claims. The core idea — reducing federated fine-tuning communication to a single sign bit via ZO + shared PRNG — is genuinely clever and well-supported by experiments spanning 11M to 13B parameters. However, the paper consistently overstates its case in two ways: (1) the exponential convergence claim is stated without qualification about the required conditions, and (2) the robustness claims are framed as general properties while the experiments cover only a thin slice of the attack/heterogeneity space. This mismatch between the strength of the framing and the specificity of the evidence is the paper's main vulnerability, not any fundamental flaw in the method itself. A revision that precisely states the assumptions behind Theorem 1 and honestly characterizes the scope of the robustness experiments would significantly strengthen the contribution.

## Suggestions

1. **Clarify communication cost precisely**: State explicitly that with shared PRNGs deterministically initialized, the per-step cost is exactly 1 bit uplink (the binary vote) and 1 bit downlink (aggregated sign). Make this statement consistent between the abstract, introduction, and conclusion.

2. **State the assumptions behind Theorem 1**: Clearly list what conditions (convexity, smoothness, PL condition, bounded noise, etc.) the exponential convergence rate requires, and discuss whether these hold in the evaluated deep learning settings. Temper the "same rate as first-order methods" claim with appropriate qualifications.

3. **Add statistical rigor to the robustness evaluation**: Include error bars over multiple seeds, test at least 2–3 levels of Dirichlet β (e.g., 0.1, 0.5, 1.0), and vary the Byzantine fraction (e.g., 20%, 40%) with at least one additional attack type (e.g., random gradients).

4. **Provide full hyperparameter specifications**: Add a table with learning rates, batch sizes, local steps, perturbation counts, and number of communication rounds for each experimental setting.

5. **Include Algorithm 1 in the main paper** (not just in Section 3, which was stripped) so the protocol is immediately clear to the reader.

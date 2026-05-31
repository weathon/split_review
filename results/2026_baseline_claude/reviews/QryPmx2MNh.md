## Summary
This paper addresses the novel task of automatically discovering learning-friendly orderings of output token sequences for Transformer models performing arithmetic tasks. The key insight is that deep neural networks exhibit easy-to-hard learning dynamics, so a short training run on a mixture of permuted target sequences allows fast identification of "easy" (learning-friendly) orderings via loss profiling. To handle the factorial search space, the authors propose a two-stage hierarchical approach (global block-level reordering followed by local intra-block refinement). The method is validated on three synthetically designed order-sensitive tasks and successfully rediscovers the known reverse-digit ordering for integer multiplication.

---

## Strengths

- **Genuinely novel problem formulation.** Automatic search for learning-friendly output-sequence permutations has not been previously studied in a systematic, automated way. The framing via the non-injective recurrence structure (Eq. 5.1) is clean and motivates the task design well.

- **Elegant core idea grounded in known learning dynamics.** Exploiting easy-to-hard dynamics to rank permutations via short-run loss profiling is simple, efficient, and empirically validated. A single epoch of training with ~1,000–5,000 mixed-order samples is sufficient to discriminate good from bad orderings (Figure 5), and this scales to the soft-permutation baseline failure case (Figure 2) that motivates why direct optimization is intractable.

- **Validation against established prior work.** Rediscovering the least-significant-digit-first ordering for PROD (Shen et al., 2023) from scratch—out of 13! ≈ 6×10⁹ candidates—provides a clean sanity check and grounds the method in a real, non-synthetic result.

- **Principled negative result.** Figure 2 carefully demonstrates why the natural soft-permutation relaxation fails (information leakage from future tokens), explicitly motivating the proposed combinatorial search over hard permutations. This is good scientific hygiene.

- **Practical computational budget.** The reported 1–7 hours on a single GPU for the longest explorations, combined with using a small 1-layer model for profiling and a larger model only for final training, makes the method plausibly applicable without massive resources.

---

## Weaknesses

### Fatal
None.

### Major

1. **Scale limitation without domain-specific initialization.** With purely random initialization (𝒫ᵣ), the method reliably recovers forward orderings only up to L=13. Scaling to L=30–40 requires structured initialization (𝒫_b), which encodes knowledge that the solution is approximately a block permutation of the forward sequence. For truly unknown tasks this prior may not be available, so the claim of handling "a few billion candidates" is somewhat misleading—it holds only when the search space is already heavily restricted by domain knowledge.

2. **Limited success on the INDEX task.** For INDEX with d=4 and d=8, the discovered orderings at L=13 are not the forward order and are not clearly explained as being "learning-friendly" in any interpretable sense (Table 2, rows for INDEX). The paper acknowledges d>2 is hard even in the forward order (Table 1), but it does not analyze whether the discovered non-forward orders actually achieve high success rates on a large model—or whether the failure is a limitation of the profiling heuristic. This gap matters because the hardest, most practically interesting cases are precisely those where the forward order is not obviously best.

3. **All tasks are synthetic with known answers.** ReLU, SQUARE-19, and INDEX are designed so that the forward order is optimal by construction. The only task where the optimal ordering was non-trivially unknown a priori is PROD (from Shen et al.). The paper does not test on any task where the discovered ordering is a genuine unknown, which limits evidence that the method produces scientifically useful discoveries rather than recoveries.

### Minor

1. **No ablation on the number of candidate permutations T.** The paper fixes T (e.g., 128 or 5,040) and reports success, but does not show sensitivity to this hyperparameter. Knowing how few candidates are needed to reliably identify good orderings would clarify the method's sample efficiency in the permutation space.

2. **Transfer from small to large models is asserted rather than systematically studied.** The claim that "learning-friendly orders must be universal" (Section 4) is plausible and empirically assumed, but not ablated. If a permutation ranked highly by the 1-layer model turns out to be suboptimal for the 6-layer model, the whole profiling stage could select the wrong ordering.

3. **L=10 random initialization failure is unexplained.** Figure 6(a) shows the discovered order for RELU at L=10 achieves only ~0.35 success rate, lower than for both L=9 and L=11. This non-monotone failure is noteworthy but not analyzed or explained.

### Trivial
None worth noting.

---

## Nice-to-Haves

- Applying the method to at least one task where no human-designed ordering is known in advance (e.g., a more complex symbolic computation) would substantially strengthen the claim of practical utility.
- A runtime analysis comparing loss profiling to exhaustive full-training over a small number of permutations would contextualize the efficiency gains more precisely.

---

## Novel Insights

The most genuinely novel observation is that the easy-to-hard learning dynamics of neural networks extend to *permutations of the output sequence*, not just to noisy labels or curriculum sample ordering—and that this property is observable within a single epoch of short training. This means that one can evaluate the "hardness" of a specific output ordering for a Transformer almost as cheaply as computing a training loss, enabling combinatorial search methods that would otherwise require full retraining. The hierarchical decomposition into global (block-level) and local (intra-block) stages is a practical engineering contribution that makes this search tractable at L=13 with random initialization. Together, these insights suggest a broader principle: Transformer learning dynamics encode structural information about the implicit causal order of a task, and that information can be read out quickly without committing to full convergence.

---

## Suggestions

- Clarify what happens with the INDEX task at d=4 and d=8: do the discovered non-forward orderings actually improve success rate when used to train the large model?
- Report the success rate of the final large-model training for all discovered orderings in Table 2, not just for select cases, so readers can judge whether profiling-based ranking reliably predicts final performance.
- Ablate T (number of candidate permutations in each profiling run) to give practitioners guidance on the cost-quality tradeoff.

---

## Score and Decision

The paper makes a clear, novel contribution by formulating and solving an automated permutation-search problem over output token orderings, grounded in a sound observation about learning dynamics. The methodology is elegant and the experimental design is mostly thorough. The primary limitations—restricted scale without domain initialization, all tasks having known optimal orderings by construction, and unexplained failure cases—are real but do not invalidate the core claims. The paper falls comfortably above the acceptance threshold for originality and execution, though it is unlikely to be transformative outside its specific niche.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
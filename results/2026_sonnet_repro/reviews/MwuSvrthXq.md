Now let me run calibration searches to score this paper properly.Now I have enough material to write the final review.

---

## Summary

WeCAN is an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility. It introduces two architectural components: (1) a Weighted Cross-Attention (WeCA) layer that multiplies compatibility coefficients *outside* the softmax to preserve task-wise compatibility profiles across varying pool counts, and (2) a Longest-Directed-Distance GNN (LDDGNN) for encoding DAG dependency structure. The paper also provides a formal analysis of the optimality gap inherent in list-scheduling-based generation maps and proposes a skip-action mechanism—theoretically backed by surjectivity arguments (Theorems 1–2)—that closes this gap while retaining single-pass efficiency. Empirical results show up to 18.1% and 13.4% makespan improvement over the best heuristics on TPC-H and Computation Graphs benchmarks, respectively, and up to 9.5% over the best neural baseline.

---

## Strengths

- **Principled WeCA design with concrete ablation support.** The outside-vs-inside placement of compatibility coefficients is motivated with a concrete example (two tasks with identical attributes but different compatibility profiles; inside-softmax yields identical embeddings, outside does not). Table 3 validates this: replacing WeCA layers in the encoder degrades makespan by 4–14% on TPC-H, and removing them entirely nearly eliminates the improvement over the Tetris heuristic (~0.5%).

- **Theoretical skip-action analysis that bridges architecture and optimality.** Section 4 frames the optimality gap via the surjectivity of the generation map: Theorem 1 proves that the skip-augmented single-pass design makes the map a surjection onto the feasible schedule space, and Figure 3 directly validates this prediction—WeCAN with skip achieves 8.3–8.9% improvement over HEFT on heavy-task benchmarks, while the no-skip variant loses ~2.3%. This is a genuine intellectual contribution to the neural CO literature.

- **Strong and consistent empirical results across diverse benchmarks.** Tables 1 and 2 show consistent improvement across TPC-H-30/50/100 and three types of Computation Graphs (Erdős-Rényi, Layer, Stochastic Block), with WeCAN-Greedy already competitive with 2-second neural baselines. The greedy mode (0.15–1.72s) matches heuristic speed while outperforming all neural baselines.

- **Robust generalization to unseen environment configurations.** Figure 2 shows WeCAN-S(256) achieving 6.7–20.4% improvement over heuristics under four types of environment perturbation (more pools, more pool types, more tasks, more task types), significantly outperforming One-Shot-S(256) (0.9–10.2%), directly validating the claimed adaptability of the WeCA architecture.

- **LDDGNN empirically superior to standard GAT variants.** Table 3 shows both forward and bidirectional GAT yield meaningfully worse makespan than LDDGNN (20747 and 20873 vs. 19908 on TPC-H-30), substantiating the design choice for DAG-aware attention.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **PRO-BALM baseline undefined.** Figure 3 shows "PRO-BALM" as a named method in the ablation on heavy-task benchmarks (achieving 4.7% and 4.5% improvement over HEFT), but this method is never introduced, cited, or described anywhere in the main text. Readers cannot determine what it represents, whether it is a heuristic, prior neural method, or an internal variant, or how to position WeCAN's results relative to it. This needs to be resolved.

- **Skip ablation absent from standard benchmarks.** The skip-action evaluation (Figure 3) is performed exclusively on the heavy-task-modified variants of TPC-H. Table 3's ablation uses the full architecture without skip (the best row "WeCA+LDDGNN" achieves makespan 19908 on TPC-H-30, vs. 18964 for WeCAN-S(256) in Table 1), yet no row labeled "WeCAN without skip" appears in the standard benchmark ablation. Whether skip provides marginal benefit on standard instances is left unanswered; this is a natural question given the theoretical analysis and would strengthen or appropriately scope the claims.

- **Missing comparison with cited heterogeneous RL baselines.** The paper specifically criticizes Wang et al. (2025) and Zhadan et al. (2023) for averaging-based compatibility embeddings, but neither appears in the experimental comparison. If these methods are incompatible with the specific problem setup, the paper should state this explicitly rather than leaving the omission implicit.

### Trivial

- **TPC-H modification underemphasized.** Section 5.1 discloses that memory constraints and task types were added to TPC-H, but this material modification is mentioned only in a single clause. A brief explicit note that results are not directly comparable to prior TPC-H work would help readers contextualize the numbers.

---

## Nice-to-Haves

- Adding a "WeCAN without skip" row to Table 3 (alongside the existing architectural ablations) would directly quantify skip's marginal contribution on standard (non-heavy-task) benchmarks, complementing Figure 3.

- The skip score functional form $u_{\pi_{skip}} = u_a(1 - k/2n)^{u_b} + u_c$ satisfies the required monotone-decreasing property, but a brief comparison to a simpler linear decay baseline (or training curve comparing skip vs. no-skip variance) would confirm that the specific polynomial decay form contributes meaningfully rather than being an arbitrary but valid choice.

- Evaluating WeCAN against an exact solver (e.g., Gurobi on the MILP formulation in Section 2.1) on small instances (e.g., 20-node problems) would provide an optimality anchor, giving the reader a sense of how much absolute gap remains.

---

## Removed Points
*These points were flagged for removal; treat with caution.*

- **"Theorem 2 is tautological"**: The harsh critic argues that Theorem 2 essentially restates Assumption 1. This is partially fair as a framing observation, but the real content—proving that the skip-augmented design satisfies Assumption 1 (Theorem 1)—is clearly novel. Removed because this is a presentation nitpick rather than a substantive flaw.

- **"Exact solver comparison essential"**: Demanding a solver comparison is reasonable as a nice-to-have but is not standard practice in the neural CO literature for medium-to-large problem sizes. Moved to nice-to-haves.

- **"Training curves showing skip reduces variance"**: An interesting supporting experiment but not required to substantiate the paper's core claims. Moved to nice-to-haves.

- **Generic strength "addresses an important problem"**: Dropped per filtering rules—too generic without paper-specific evidence.

---

## Novel Insights

The paper's most genuinely novel contribution is the formalization of the optimality gap in list-scheduling-based neural methods via the injectivity/surjectivity lens (Section 4). The framework of analyzing whether a generation map $S : B_f \to A$ satisfies $TS = I$ and $f(v) \geq f(ST(v))$ is not specific to WeCAN and can serve as a general diagnostic for other neural schedulers. The insight that poor solutions concentrate in the high-$u_a$, high-$u_c$ region of the skip-augmented space—making variance controllable—is an underappreciated structural argument that would generalize to other action-augmentation designs in single-pass neural CO settings.

---

## Suggestions

1. Introduce and cite PRO-BALM in the main text (or remove it from Figure 3 if it is not relevant).
2. Add a "WeCAN without skip" row in Table 3 on the standard benchmarks to quantify skip's marginal benefit outside the heavy-task scenario.
3. Briefly state why Wang et al. (2025) and Zhadan et al. (2023) are not included in the experiment tables (e.g., incompatible MDP formulation, multi-pass inference), since the paper explicitly critiques these methods in Section 1.
4. Add a single sentence clarifying that TPC-H results are not directly comparable to the original benchmark due to added constraints.

---

## Score and Decision

**Calibration anchors retrieved:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Simultaneous Gen+Improve RL FJSP | 10eQ4Cfh8p.md | 3.00 | R1 weak | Clearly weaker than WeCAN — no theoretical analysis, weaker baselines |
| Massively Parallel CO RL | CJEBFNBLhO.md | 4.25 | R1 mid | Weaker — engineering contribution without WeCAN's theory or empirical depth |
| Multi-task Neural CO | Dgc5RWZwTR.md | 4.75 | R1 mid | Weaker — multi-task training novelty but less rigorous architecture/theory |
| RL Quantum Resource Scheduling | 8WtBrv2k2b.md | 5.00 | R2 | Weaker — domain-specific application without WeCAN's architectural/theoretical depth |
| Neural Solver Selection for CO | CFLEIeX7iK.md | 5.75 | R2 | Somewhat comparable in addressing a gap in CO; less novel theoretically |
| CCBPP Encoder-Decoder | 6hvtSLkKeZ.md | 6.40 | R2 | Comparable — introduces new problem variant + method + ablations, but WeCAN has stronger theory and better generalization |
| Symb4CO Symbolic CO Discovery | jKhNBulNMh.md | 6.67 | R2 | WeCAN is comparable — both have architectural novelty, theoretical backing, strong empirical results; WeCAN has a more complete ablation study |
| Minimalistic Predictions Online Scheduling | j8lqABLgub.md | 6.00 | R2 | Weaker — scheduling theory paper without WeCAN's empirical breadth |

**Round 1 bracket:** 5.0–7.5, with most NCO papers in this tier scoring 5–7.

**Round 2 narrowing:** The most topically close anchors in the bracket are jKhNBulNMh (6.67) and 6hvtSLkKeZ (6.40). WeCAN is comparable to Symb4CO: both present architectural/theoretical contributions to CO, achieve strong and consistent empirical gains over both heuristics and neural baselines, and include thorough ablations. WeCAN's theoretical analysis (surjectivity/optimality gap formalism) is arguably more sophisticated than Symb4CO's symbolic discovery component. The primary weaknesses—undefined PRO-BALM, missing skip ablation on standard benchmarks, absent comparisons with two cited baselines—are real but addressable in author response; none invalidates the core contribution. WeCAN is at least as strong as jKhNBulNMh (6.67) and I place it slightly above that anchor given the theoretical depth and more comprehensive evaluation.

**Final score: 6.5 (Accept)**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
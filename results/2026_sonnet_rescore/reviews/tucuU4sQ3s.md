## Summary

NuSA-CL is a memory-free continual learning framework for CLIP-based vision-language models. It confines low-rank weight updates to the approximate null space of current parameters (identified via SVD), merges the update into the backbone after each task, and repeats the cycle—maintaining a fixed parameter budget with zero storage overhead. On the MTIL benchmark NuSA-CL achieves 68.6%/75.1%/82.8% Transfer/Avg./Last with only 1.5M trainable parameters and 1.21 GPU-hours, approaching storage-based methods at a fraction of their cost, and on 50-step CIFAR-100 it outperforms the next-best baseline by 4.4% in Last accuracy.

---

## Strengths

- **Theoretical interference bounds (Lemma 1, Theorem 2, Eqs. 5–6):** The paper quantifies cumulative parameter-level interference: $\sum_{t=1}^T |\langle W_{t-1}, \Delta W_t \rangle_F| \leq \sum_{t=1}^T \sigma_{t,\max}^{\text{null}} \cdot \|M_t\|_F$. The proof is valid and tight given the formulation, and the paper is appropriately upfront that this is a parameter-space rather than function-space bound (Section 4.2).

- **Efficiency-performance trade-off is compelling (Table 1):** NuSA-CL uses 40× fewer parameters than MoE-Adapters (1.5M vs. 59.8M), zero additional storage vs. 10.5 GB for ZSCL, and nearly 3× less compute (1.21 vs. 3.42 GPU-hours), while matching or exceeding storage-free baselines by large margins (Transfer: 68.6% vs. 63.9% for LoRA; Last: 82.8% vs. 79.9% for LoRA).

- **Null-space dynamics provide quantitative evidence (Figure 2):** The effective rank of NuSA-CL's weights increases consistently from ~57.9% to ~58.8% (text encoder) and ~51.8% to ~52.4% (vision encoder) across 10 tasks, while LoRA and Full-FT remain nearly static (e.g., LoRA vision output projection: 447.42 → 447.58 effective rank). This is a concrete, per-layer spectral signature directly distinguishing NuSA-CL from alternatives.

- **Ablations validate core design choices (Figure 3, Table 4a):** Tail (null-like) subspace achieves 2.57% forgetting vs. 4.44% (Top) and 4.57% (Random) at rank 128. Unfreezing the null-space bases $(U_n, V_n)$ drops Transfer from 68.58% to 62.60%, validating the persistent constraint as essential. The result that making bases trainable so severely hurts performance is a particularly informative ablation.

- **Computational practicality demonstrated (Table 4b):** SVD initialization takes < 1 minute per task vs. ~81 minutes for InflLoRA's data-dependent gradient projection, while NuSA-CL still achieves higher Avg. accuracy (75.1% vs. 74.2%).

---

## Weaknesses

### Fatal
None.

### Major

- **Missing matched-parameter-count baseline.** NuSA-CL has 1.5M trainable parameters while LoRA and MiLoRA have 15.7M (Table 1), a roughly 10× difference. A method with substantially fewer degrees of freedom is inherently more regularized and will overfit to each new task less aggressively—which is itself a mechanism for reducing forgetting, independent of the null-space design choice. The rank ablation in Figure 3b shows that performance does not consistently improve beyond rank 128 and Transfer even declines at rank 196 and 256, consistent with the implicit-regularization interpretation. Without a baseline of LoRA with rank ~16 (matching NuSA-CL's ~1.5M parameters), it is impossible to attribute the performance gains to the *null-space constraint* specifically rather than to the *stronger implicit regularization* from having far fewer trainable parameters. This does not invalidate the method—which also legitimately claims an efficiency advantage—but it leaves the mechanistic claim undetermined.

- **Core cross-task protection mechanism is never articulated.** The paper's central practical benefit is that knowledge from task $t$ is not overwritten by task $t+1$. The theoretical analysis (Section 4) bounds parameter-space interference per-step, which the paper rightly limits to a "local stability condition." However, the *sequential* protection mechanism is never explained: when $\Delta W_t = U_{t-1,n} M_t V_{t-1,n}^\top$ is merged into $W_{t-1}$ to produce $W_t$, those previously null-space directions receive increased spectral energy and are promoted into $W_t$'s principal subspace. The SVD for task $t+1$ then places them in the *principal* subspace, not the null space, so the task-$(t+1)$ update is constrained to avoid them by construction. Figure 2's progressive effective-rank increase is precisely the empirical signature of this mechanism, but the paper describes it as "knowledge accumulation" without explaining why it implies protection from future updates. Section 3.3 says the cycle "repeats" and the null space is "dynamically identified" but treats the protection argument as self-evident. The theory in Section 4 does not formalize this cross-task property. This is the core "why does it work" question, and its absence makes the theoretical contribution thinner than it could be.

### Minor

- **10-step CIFAR-100 Avg. results not discussed.** In Table 3, ZSCL achieves 82.15% Avg. at 10 steps while NuSA-CL achieves 80.25%, meaning ZSCL retains higher average accuracy across all 10 tasks in the short-sequence regime. NuSA-CL wins on Last (74.51% vs. 73.65%). The paper only highlights the 50-step result and does not acknowledge that the advantage materializes with longer sequences—valuable information for practitioners choosing between methods in short vs. long task sequences.

### Trivial

- **Terminology inconsistency: "intrinsic null space" vs. "approximate null space."** Using ρ=0.95 energy cutoff means σ_{k+1} > 0 (as Lemma 1 itself makes explicit). The paper alternates between "intrinsic null space," "approximate null space," and "low-energy subspace." Consistent use of "approximate null space" or "low-energy subspace" throughout would improve precision without affecting any technical claim.

---

## Nice-to-Haves

- **Matched-rank LoRA baseline** (rank ~16 to achieve ~1.5M parameters): would cleanly separate the contribution of the null-space constraint from the contribution of implicit regularization. Given that this single ablation would substantively strengthen the main claim, it is worth prioritizing.

- **Brief task-order sensitivity experiment** (2–3 MTIL permutations): all results use a fixed task ordering. Even a brief robustness check on two permutations would address this limitation, which the paper itself flags as future work.

- **Explicit articulation of the merge-promotes-to-principal-subspace mechanism** in Section 3.3 or Section 6.1: formalizing or at least stating this argument clearly would make the theoretical narrative significantly more complete and align the text with the observed Figure 2 dynamics.

---

## Removed Points

*These points are flagged as removed — treat them with caution.*

- **Harsh Critic — parameter-space theory overstated:** The critic argued the paper overclaims by framing parameter-space bounds as a "principled mechanism for mitigating catastrophic forgetting." However, Section 4.2 explicitly says: *"We emphasize that the above results are stated in parameter space and should be viewed as a local stability condition rather than a full function-level guarantee."* The paper is transparent about this. Removed as a standalone weakness since it is already acknowledged.

- **Harsh Critic — LoRA effective rank of 447.42 → 447.58 may be within noise:** While technically valid that a 0.16 change is small, the paper uses this number to illustrate a trend that is consistent across all layers (Figure 2) and discusses the full-layer pattern. The point is superseded by the broader, more compelling evidence in Figure 2. Removed as insufficient basis for a standalone criticism.

- **Harsh Critic — "decisive" framing of NuSA-CL over InflLoRA:** Section 5.2 calls the win over InflLoRA "decisive." Looking at Table 2, the Transfer gap is 68.1 vs. 66.8 (1.3%) and Last is 75.4 vs. 74.8 (0.6%), and Aircraft is 27.2 vs. 21.9. The framing is slightly strong but NuSA-CL consistently leads across metrics while being storage-free vs. InflLoRA being storage-based. Not a substantive concern—removed as a minor framing nitpick.

- **Strength Finder — importance of the research question:** Removed as a generic strength that does not cite specific evidence from the paper.

---

## Novel Insights

The most genuinely novel observation surfacing from this review—not stated by the paper itself—is the implicit **merge-as-subspace-promotion** mechanism: constraining updates to the null space and then merging them into the weights necessarily elevates those directions' spectral energy, causing them to migrate into the principal subspace before the next task's SVD. This creates a passive, automatic "write-protect" effect on prior knowledge without any explicit memory or regularization. The paper implicitly relies on this mechanism (Figure 2 documents it quantitatively), but neither articulates it nor formalizes it. If stated explicitly, this would significantly clarify why NuSA-CL improves over time compared to methods that merely use the null space for initialization.

---

## Suggestions

1. **Add a LoRA-at-rank-16 baseline** (matching NuSA-CL's ~1.5M parameter count) to Table 1 or the ablation section, and discuss whether the null-space constraint adds value beyond the implicit regularization from fewer parameters.

2. **Articulate the merge-promotes-to-principal-subspace mechanism** in Section 3.3, even in one or two sentences. Something like: "Note that after merging, the directions that were previously in the null space of $W_{t-1}$ now carry spectral energy in $W_t$, causing the next SVD to place them in $W_t$'s principal subspace, thereby protecting them from overwriting by future updates." This single addition would substantially improve the theoretical coherence.

3. **Address the 10-step CIFAR-100 Avg. result** (80.25% vs. ZSCL's 82.15%) explicitly in Section 5.2 or the analysis, clarifying under which conditions NuSA-CL's advantage emerges (longer sequences) and where it is less pronounced.

4. **Harmonize terminology** throughout: use "approximate null space" or "low-energy subspace" consistently instead of alternating with "intrinsic null space."

---

## Score and Decision

**Originality:** The core idea of confining updates to the SVD-derived low-energy subspace is related to prior orthogonal projection work and MiLoRA, but the persistent-constraint + merge cycle for zero-memory CL is a genuinely novel combination. **3/5**

**Importance:** Memory-free CL for VLMs under fixed parameter budgets is a practically important setting, especially as VLMs become backbones for embedded and edge systems. **4/5**

**Claims supported:** The empirical results clearly support the efficiency-performance tradeoff claim. The mechanistic claim (null-space constraint drives forgetting reduction) is partially supported by ablations but the parameter-count confound means the attribution is not fully established. **3/5**

**Soundness:** The method is technically correct. The theory is honest about its scope. The main soundness concern is the unaddressed parameter-count confound. **3/5**

**Clarity:** Well-written, structured clearly, with honest acknowledgment of limitations. The gap in the mechanistic narrative (Section 3.3/6.1) is the main clarity issue. **4/5**

**Community value:** Concrete benchmark results, reproducible 3-step method, practical guidance, and a framework others can build on. Strong value for the CL-for-VLMs community. **4/5**

Overall this is a solid, well-executed contribution. The two major weaknesses (missing matched-parameter baseline and incomplete mechanistic explanation) are addressable in a revision and do not invalidate the core results, which are strong. The paper merits acceptance, particularly for its favorable empirical results and practical contributions, contingent on engagement with the parameter-count confound.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
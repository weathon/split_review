- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

ER-AAE proposes a two-stage classical algorithm for approximate amplitude encoding: (1) a greedy circuit construction stage that iteratively adds CZ-containing two-qubit gates to reduce the linear entropy of the target state, and (2) an infidelity-minimization fine-tuning stage. The method uses only a single CZ per two-qubit gate (versus 2–3 CNOT/CZ needed for decomposing general two-qubit unitaries) and provides a theoretical bound connecting the final infidelity to the linear entropy of intermediate states. Experiments on MNIST, CIFAR-10, random vectors, and random quantum circuit states claim lower infidelity and higher PSNR than MPS, AQCE, AQCE-MPS, ADAPT-VQE, and hardware-efficient baselines.

## Strengths

- **Novel entropy-driven circuit construction** — The greedy search that selects gates to maximally reduce linear entropy is a principled alternative to prior heuristic approaches (MPS, AQCE) that do not explicitly optimize circuit architecture based on entanglement properties. The per-gate optimization involves only 4 parameters, making the classical preprocessing tractable.

- **Theoretical guarantee connecting fidelity to linear entropy (Proposition 2)** — The bound \(|\langle v_{\text{target}}|V(\theta)|0\rangle|^2 \geq 2^{\lfloor -2L\rfloor}\) provides a rigorous (if coarse) connection between the achievable infidelity and the entanglement reduction achieved during circuit construction. This is a theoretical anchor missing from prior AAE heuristics.

- **TN initialization with proven non-vanishing fidelity (Proposition 1)** — The tensor-network-based initialization of the final single-qubit unitary layer guarantees that the initial fidelity is bounded away from zero, mitigating barren-plateau issues during fine-tuning. Figure 2(b) provides empirical verification.

- **Interesting empirical finding about real-world data** — Figure 2(a) shows that linear entropy decays significantly faster for MNIST and CIFAR-10 images than for random vectors during the entropy-reduction stage. This observation could be independently useful for future AAE research.

- **Gate-efficiency by design** — Each ER-AAE two-qubit gate contains exactly one CZ gate (plus four single-qubit rotations), whereas prior methods build circuits from general two-qubit unitaries that decompose into 2–3 CNOT/CZ gates. This structural choice is well-motivated for NISQ hardware with limited two-qubit gate fidelities.

## Weaknesses

### Fatal
None.

### Major

- **Missing statistical measures for all results** — Figures 2–3 and Tables 2–3 report only point averages (over 10 or 50 samples) with no standard deviations, confidence intervals, or error bars. The reader cannot assess whether the reported superiority of ER-AAE is statistically significant, nor can the reliability of the entropy-decay trends be evaluated. This is the single most important evidential gap in the paper.

- **Unequal optimization budget across methods** — ADAPT-VQE is given only 1,000 training iterations, while ER-AAE's infidelity minimization uses 10,000 iterations (a 10× difference). HE circuits also receive 10,000 iterations. No analysis is provided to show that ADAPT-VQE has converged at 1,000 iterations, nor is it explained why this disparity is justified. This asymmetrically disadvantages a key baseline.

- **Gate-count comparison requires clarification** — The paper claims ER-AAE achieves "lower error with an equivalent or fewer number of CNOT or CZ gates." Table 1 lists "feasible numbers of CNOT/CZ gates" for each method. However, since Table 1 is an embedded image, the reader cannot verify whether the counts for MPS, AQCE, and AQCE-MPS correctly reflect the 2–3× decomposition cost of their general two-qubit unitaries (which the paper text acknowledges on line 172). If the table counts two-qubit unitaries rather than the actual number of CNOT/CZ gates after decomposition, the comparison would systematically favor ER-AAE. This ambiguity undermines the paper's central comparative claim and must be resolved.

### Minor

- **ADAPT-VQE convergence uncertainty** — Beyond the iteration count mismatch, the paper does not report whether any baseline has reached a stationary point in optimization. The 10,000-iteration budget for ER-AAE and HE may be excessive or insufficient; without convergence curves or stopping criteria, the reader cannot judge.

- **Proposition 2 bound is coarse** — The bound \(2^{\lfloor -2L\rfloor}\) steps down in coarse increments (e.g., it is constant at 0.5 for all \(L < 0.5\)). While any guarantee is valuable, this one is too loose to provide practical guidance about the number of gates needed for a target fidelity.

- **No hyperparameter sensitivity analysis** — The learning rate (0.01) and iteration counts are fixed across all methods and stages. No evidence shows that these choices are appropriate for each method, or that the results are robust to their variation.

- **Gate slide \(C_{ER}=1\) implies high classical cost** — With \(C_{ER}=1\), optimization of ALL accumulated gates (up to 100) is performed after every single gate addition. The paper does not discuss the total classical computational cost or compare it to baselines.

### Trivial
- The paper contains minor formatting artifacts (garbled characters in equations) attributable to the PDF extraction process, not the original submission.

## Nice-to-Haves
- A small ablation study showing that the greedy entropy-reduction stage (as opposed to random or structured circuits with the same number of CZ gates) is responsible for the fine-tuning success.
- Wall-clock time comparisons to quantify the classical preprocessing cost relative to baselines.
- Sensitivity analysis of the learning rate and training iterations.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- **Gate-count comparison as a confirmed "structural flaw"** (Harsh Critic Point 1): The critic asserts that Table 1 "counts these unitaries as single CNOT/CZ gates rather than accounting for their decomposition cost." This is an assumption that cannot be verified from the paper text. The paper explicitly discusses decomposition costs (line 172: "the decomposition of arbitrary two-qubit unitary requires two and three CNOT/CZ gates") and Table 1 is explicitly titled "Feasible numbers of CNOT/CZ gates used in different encoding methods." I have demoted this from "Fatal/Structural" to a Major concern requiring clarification, because the critic's stronger claim is not verifiable from the available evidence.

- **Proposition 2 being "quite weak" / "not sharp enough" as a weakness** — This is an observation about the nature of the bound, not a flaw. The bound is what it is; it still provides a non-trivial guarantee connecting circuit performance to entanglement reduction. Retained only as a minor observation.

- **Missing related work mentions** — Cannot verify without external literature access.

- **Reproducibility concerns about undisclosed hyperparameters (BFGS tolerance, etc.)** — These are minor implementation details common in ML/quantum papers; demanding complete logs is excessive.

- **Code release / data splits** — Not required for review; reproducibility assessments should not hinge on code availability for a conference submission.

- **"Strengthening the Paper on Its Own Terms" suggestions** — These are constructive suggestions, not weaknesses. Partially absorbed into Nice-to-Haves.

- **Strength Finder's claim about "consistent empirical outperformance"** — The paper claims this, but since the actual tables/figures are images, I note this as a claimed strength with the caveats described above.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the main strengths (novel entropy-reduction approach, theoretical bound, interesting real-world data observation) and weaknesses (missing error bars, unequal baseline comparisons, gate-count ambiguity). The most useful cross-review insight is that the gate-count concern, if confirmed, would cut deeper than the missing error bars — but since Table 1 is an image, neither reviewer nor meta-reviewer can definitively resolve it from the available text.

## Suggestions

1. **Report error bars** (standard deviations or confidence intervals) for all main experimental results. With only 10–50 samples per condition, this is essential for interpretability.
2. **Equalize optimization budgets or provide convergence evidence** for all baselines. If ADAPT-VQE genuinely converges faster, show this with learning curves.
3. **Clarify Table 1 explicitly**: state whether the reported numbers for MPS, AQCE, and AQCE-MPS correspond to (a) the count of general two-qubit unitaries before decomposition, or (b) the equivalent number of CNOT/CZ gates after decomposition (factoring in the 2–3× multiplier). If (a), recompute all comparisons at equal CNOT/CZ counts.
4. **Discuss the computational cost of \(C_{ER}=1\)** and whether a sparser gate slide (e.g., \(C_{ER}=10\) or \(C_{ER}=20\)) achieves similar results.
5. **Add an ablation** comparing ER-AAE's greedy entropy reduction against random gate selection with the same number of CZ gates and the same fine-tuning protocol, to isolate the benefit of the greedy search.

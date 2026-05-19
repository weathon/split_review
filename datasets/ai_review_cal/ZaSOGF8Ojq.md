- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Now I have thoroughly verified all claims against the paper. Let me write the consolidated review.

## Summary

The paper proposes TOPING, a framework for intrinsically interpretable graph learning that uses persistent homology to learn a filtration function separating rationale subgraphs from noise. The core idea is novel: model the graph as "growing" from a core rationale, learn importance scores via a GNN, and maximize the topological discrepancy (measured via persistence diagrams) between rationale and noise subgraphs. The paper provides theoretical claims about unique optimality and reports large empirical gains.

## Strengths

- **Novel application of persistent homology to intrinsic graph interpretability**: Using a learned filtration to separate rationale from noise via topological discrepancy is a creative and well-motivated approach. The idea of modeling graph generation as a filtration process and maximizing the persistent gap between rationale and complement graphs is original and addresses a genuine limitation of prior methods (variiform rationales).

- **Direct empirical evidence for handling variiform rationales**: Figure 3 on BA-HouseOrGrid-nRnd demonstrates that as the number of rationale subgraphs increases, TOPING's interpretation AUC remains stable while GSAT, DIR, and GMT-Lin degrade substantially. This is the paper's strongest experimental result, as it directly targets the core claim.

- **Tractable approximation with theoretical grounding**: Theorem 3.2 provides a lower bound via Kantorovich duality (approximated by learnable Lipschitz vectorization functions with multi-head attention) and an upper bound via Gromov-Hausdorff stability, giving the topological discrepancy a principled differentiable formulation.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled backbone comparison between TOPING and baselines**: The experimental setup states "GIN is used as the backbone model for baselines" and "We first apply CINPP as our backbone to test the wide applicability of TOPING" (line 190). If TOPING uses CINPP while all baselines (DIR, GSAT, GMT-Lin) use GIN, the reported improvements cannot be attributed to the proposed topological loss—they may reflect backbone capacity differences. The paper does not report TOPING with a GIN backbone, nor CINPP-based baselines. Given that very large gaps are reported (e.g., "nearly 20% improvement"), the central empirical claim is not supported by the evidence as presented. *Evidence: line 190–191.*

- **Theorem 3.4 stated without proof or proof sketch**: The paper claims "the proof is a bit technical" (line 139) and provides no argument, not even a high-level sketch. Since Theorem 3.4 is central to the paper's claim of a "solid theoretical foundation" and is cited in multiple places as establishing unique optimality, the absence of any proof—or even an outline of the reasoning—makes the theoretical contribution unverifiable. *Evidence: lines 139–143.*

### Minor

- **Ambiguous filtration notation in method description**: The paper defines a standard filtration G≤t = {e: f(e) ≤ t} in Section 2.3, but in Section 3 the ordering follows 1−f(e) while G_X is extracted as G_{<0.5}. Whether the threshold 0.5 applies to f(e) or the transformed value 1−f(e) is unclear from the notation alone. The intent (rationale edges have f(e) > 0.5 and appear earlier) is inferable from context and Figure 1, but the inconsistent notation creates unnecessary confusion about the core mechanism. *Evidence: lines 58, 91, 111.*

- **Numerical variance not reported**: Results are averaged over 5 runs and the shadowing criterion (mean−1×std) implies standard deviations exist, but numerical std values are not shown in the text. While the tables (as images) may contain this information, the lack of explicit numerical variance reporting makes it harder to assess result reliability, especially for the large reported gains. *Evidence: lines 192, 205, 209.*

### Trivial
- The related work (Section 3.3) is placed inside the method section rather than having its own section; this is a minor organizational issue.

## Nice-to-Haves
- Adding TOPING results with a GIN backbone (matching the baselines) would directly address the backbone fairness concern.
- A proof sketch for Theorem 3.4, even 2–3 sentences outlining the key steps, would substantially strengthen the theoretical contribution.
- Runtime comparisons would be helpful given the paper's own acknowledgment of computational cost as a limitation.

## Removed Points

- **"Method description is internally inconsistent / impossible to reproduce"** — The critic claimed the filtration construction contains a contradiction. While the notation is sloppy (using G_{<0.5} without clarifying the filtration value), the core mechanism is discernible: edges are ordered by 1−f(e) and those with f(e) > 0.5 form G_X. Demoted from "fatal" to Minor.
- **"Results appear implausibly strong"** — Speculation about near-perfect scores without variance is not a verified weakness. The paper does report 5-run averaging and uses a std-based shadowing criterion. Removed.
- **"Abstract overstates results"** — The claim is "up to 20%+," which is supported for the spurious motif datasets where the largest gains occur. Smaller gains on Mutag do not contradict "up to." Removed.
- **"Shadowed entries not visible"** — Parser artifact; the original submission has visible figures/tables. Removed.
- **"Table 3 missing"** — Parser strips supplementary content; exists in the original. Removed.
- **"DIR does not assume invariance"** — Factually incorrect; DIR is built on the invariant rationale assumption. Removed.
- **"Related work inside method section"** — Pure formatting preference. Removed.
- **"Oversimplifies existing methods"** — Subjective opinion without concrete evidence of factual error. Removed.
- **General area sweeps** (e.g., "evaluation lacks rigor" without concrete anchor, "could the metric be measuring a proxy") — Removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same core issues (backbone fairness, missing proof, notation clarity) and the same strengths (novelty of the topological approach, variiform rationale experiments). The harsh critic correctly identifies the backbone mismatch and missing proof as the most serious concerns; the strength finder correctly identifies the variiform rationale experiments and the tractable lower bound approximation as genuine contributions.

## Suggestions

1. **Clarify the backbone setup explicitly**: State clearly whether TOPING uses GIN or CINPP in the main results. If the main results use GIN (like baselines), say so. If they use CINPP, include controlled experiments (TOPING with GIN, or baselines with CINPP) to isolate the effect of the topological loss.
2. **Provide a proof sketch for Theorem 3.4**: Even a brief outline of the argument (e.g., how the condition |E_X| < |E_ε| interacts with the topological discrepancy to force the unique solution) would make the theoretical contribution verifiable.
3. **Resolve the notation for G_X extraction**: Unambiguously state that G_X = {e: f(e) > 0.5} (or equivalently, edges appearing before step 0.5 in the ordering based on 1−f(e)).
4. **Report numerical standard deviations** alongside mean values in tables for all datasets.

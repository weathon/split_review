Now I have a thorough understanding of the paper and anchors. Let me write the consolidated review.

---

## Summary

This paper identifies post-treatment selection as an underexplored challenge in interventional causal discovery, where samples are selectively retained after interventions (e.g., quality control in gene perturbation studies). The authors show that existing frameworks cannot distinguish causal relations from post-treatment selection because both produce the same invariance/variability patterns. They introduce a new formulation modeling selection within augmented DAGs, define a fine-grained interventional Markov equivalence class (FI-Markov), propose the F-PAG graphical representation with novel edge marks, and develop a sound-and-complete algorithm (F-FCI) to recover causal structure from observational and interventional data. Experiments on synthetic and real-world gene perturbation data demonstrate improved precision and SHD over existing methods.

## Strengths

- **Identifies a genuine, underexplored problem.** Post-treatment selection (distinct from pre-treatment selection or standard latent confounding) is clearly motivated via Figure 1, Figure 2(c)-(e), and the discussion in §2.2. The paper makes a compelling case that existing interventional frameworks place causally distinct structures in the same equivalence class, and the running examples (Figures 1, 4, 5) make this concrete.

- **Provides a coherent theoretical framework with novel equivalence class and graphical representation.** The extension of augmented DAGs to include selection variables (Definition 1), the characterization of Markov properties linking d-separation to CI patterns (Theorem 1, Lemma 1), and the graphical criteria for FI-Markov equivalence (Lemmas 2–4, Theorem 2) build systematically on established causal discovery foundations. The F-PAG (Definition 5) represents a genuine attempt to encode finer structural distinctions than standard PAGs.

- **Empirical evidence of improvement over baselines.** Figure 6 shows F-FCI achieving higher DAG precision and lower SHD than six existing methods (GIES, JCI-GSP, IGSP, UT-IGSP, FCI-interven, CDIS) across varying dimensions and sample sizes, under both hard and soft interventions. The consistent margin (roughly 5% precision improvement) across configurations is noteworthy.

## Weaknesses

### Fatal
None.

### Major

- **The F-PAG edge mark definitions are imprecise, weakening the paper's central representational contribution.** Definition 5 lists four marks and eight edge types, but the square mark (□) is described as "a node with at least one tail and at least one arrowhead" — this is not a standard edge-endpoint property and its operational meaning in terms of conditional independence constraints is never systematically stated. The ▲ mark is described qualitatively (lines 193-194: "inducing paths that have the same CI patterns with tail/arrowhead, but without a direct causal link and selection separately") but without a formal mapping to which augmented DAG substructures produce it. As a result, a reader cannot verify from the main text alone what information each F-PAG edge type encodes. This is not fatal because the core idea (that interventional data enables finer distinctions) is clear from Figures 4-5, but the formal representational apparatus — which is one of the paper's three claimed contributions — is underspecified.

- **The experimental metric computation is not described, undermining confidence in the quantitative results.** The paper reports "DAG Precision" and "DAG SHD" (Figure 6) but never explains how the F-PAG output (with non-standard edge marks like □, ▲, Δ) is mapped to an adjacency matrix comparable against ground-truth direct causal edges. The same issue applies to baselines like FCI-interven (which outputs a PAG). For example, do □-marked edges count as causal edges? Are they excluded? Without this mapping, the reported gaps cannot be fully interpreted. This is a substantive specification gap, not a minor detail.

### Minor

- **The core reasoning in §3.2 about how Type I inducing nodes enable disambiguation is compressed and informal.** The key insight — that hard interventions on X₃ (a Type I inducing node) block selection effects on latent confounders, allowing ψ₃ ⟂̸ X₂ to distinguish causation from selection — is conveyed qualitatively over a few sentences (lines 137-138). While the algorithmic use of this insight is detailed in Step 2.3, no lemma or theorem in the main text formalizes the graphical conditions under which this test is necessary and sufficient. The soundness/completeness theorems (Theorems 3-4) are stated without proof sketches in the main body, which is understandable given space but leaves the theoretical justification somewhat opaque.

- **The real-world experiment (Section 5.2) lacks comparison with baselines.** Only F-FCI is applied to the Norman dataset and evaluated against Enrichr prior knowledge; none of the six baselines from the synthetic experiments are compared. The results are deferred to the appendix (Figure 13, Appendix D.3), so the main text provides no quantitative evidence of real-world advantage over existing methods.

- **No ablation isolating the Type I inducing node refinement (Step 2.3).** The algorithm's claimed advance over standard invariance-based orientation comes from Step 2.3, yet the paper provides no experiment showing F-FCI's performance with Step 2.3 disabled. Without this, it is unclear whether gains come from the novel selection-resolution mechanism or from standard interventional orientation rules already partially present in baselines like FCI-interven.

### Trivial

- Notation inconsistency: the specialized edge marks appear as both Δ→ (line 241, 256) and ▲→ (line 193, 256), which may confuse readers trying to map between the F-PAG definition and the algorithm pseudocode.

## Nice-to-Haves

- A sensitivity analysis of the method's performance to CI test power / finite-sample errors would strengthen the practical case, since the theory assumes oracle CI tests.

- A discussion of how often Type I inducing nodes occur in typical graph structures, and what F-FCI can recover when they are absent, would help practitioners assess applicability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The core algorithmic method and graphical representation are presented so incompletely that the paper's main contribution cannot be evaluated."** — Overstated. The F-PAG is defined (Definition 5), the marks are explained (lines 193-197), and Figure 5 provides visual illustration. The presentation could be more precise but is not "impossible to evaluate."

- **"The orientation rules in Step 2.2 are garbled and illegible"** — This is a PDF extraction artifact. All six rules show identical "(⊥,⊥,⊥,⊥)" text because the ✓/✗ symbols from the original paper did not survive the parser. The actual CI pattern table is correctly rendered in Figure 4 (lines 111-117). This is not an author error.

- **"The novel edge marks (Δ‑arrow, ▲‑arrow) are introduced without ever being defined in the paper's body"** — Incorrect. They are defined at line 256 and used in the algorithm pseudocode (lines 241, 245), and their relationship to Figure 5's structures is explained.

- **"The definition of Type I inducing node (Def. 6) is circular and obscure"** — Definition 6 (lines 195-196) defines Type I as "an incoming arrowhead into a square (—□)" on a non-endpoint node of an inducing path, with Figure 5 providing a concrete example (X₃ in Figure 5(b)). While terse, it is not circular.

- **"No formal theorem or lemma is provided that specifies the general graphical conditions" for Type I node tests** — The harsh critic argues that the paper lacks a provable identification condition for the multi-variable intervention test. However, Theorems 3-4 claim soundness and completeness, and the proofs exist in the appendix (stripped by the parser). The critique about insufficient proof sketches in the main text is retained as a minor weakness above, but the claim that no formal foundation exists is inaccurate.

- **Strength Finder: "this paper is well written"** — Dropped as generic.

- **Strength Finder: "Transparent discussion of assumptions and limitations"** — Partially true (the limitation about Type I inducing nodes is acknowledged), but the discussion is brief (two sentences in §6). Kept in spirit via the minor weakness about missing ablation.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface a genuinely novel meta-insight. The paper's core observation — that post-treatment selection and causation produce identical invariance patterns under existing frameworks, and that structural asymmetries exploitable through multi-variable interventions can break this symmetry — is the paper's own contribution and is well-articulated.

## Suggestions

- Provide a table or formal mapping that explicitly associates each F-PAG edge type (—, ▲, □—□, etc.) with the set of augmented DAG substructures and CI patterns it encodes. This would resolve the imprecision in Definition 5 and make the representation independently usable.

- In the experiments section, add a clear sentence defining what counts as a "true positive" edge for DAG Precision/SHD: e.g., "We evaluate direct causal edges only; edges marked with □ or ▲ in the F-PAG are considered non-causal for metric computation." This is one sentence that would close the metric specification gap.

- Add a one-paragraph proof sketch for Theorems 3-4 in the main text, even if the full proofs remain in the appendix. Currently the transition from the algorithm description to the soundness/completeness claims feels abrupt.

- Run F-FCI with Step 2.3 disabled and report results as an ablation; this would directly quantify the contribution of the Type I inducing node refinement.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| mA78uXqcnl (Causal Structure Learning in Hawkes Processes) | 7.00 | More polished theory, clearer exposition, stronger experiments. Current paper has comparable ambition but less precise definitions and less thorough real-world validation. |
| kK7PbRzqGk (Efficient Learning on Large Graphs) | 7.00 | Different domain; both have novel theoretical contributions. Current paper's novelty is at least as high but execution is less polished. |
| s0nYSwlV3I (Influence without Confounding) | 5.00 | Similar structure: novel problem formulation, theoretical framework, algorithm, synthetic + limited real-world experiments. Current paper has broader synthetic experiments and a soundness/completeness proof. |
| V7pT2ZRoTB (Theoretical Guarantees for CD) | 4.50 | Narrow theoretical contribution with limited empirical scope. Current paper has broader contribution and stronger empirical validation. |
| lYearSsgXj (Coupled Confounding and Collider Biases) | 4.50 | Novel problem formulation but strong, hard-to-verify assumptions. Current paper's assumptions are more standard in causal discovery. |
| HfiRzzmFt8 (ABCDEFG) | 4.00 | Novel approach but unclear motivation for framework choice. Current paper has clearer motivation and more grounded theoretical development. |
| Ja0jG1Pvtg (DAG DECORation) | 4.00 | Theoretical contribution with experimental validation. Current paper has stronger novelty and broader scope. |
| r4TvgVFo9L (InvarGC) | 3.50 | Imprecise assumptions, limited novelty. Current paper is substantially stronger. |
| nSuJ4OXf0j (CIT-TBP) | 2.50 | Confusing core assumptions, limited contribution. Current paper is much stronger in both theory and experiments. |

The paper has genuine novelty (identifying and formalizing post-treatment selection as a distinct challenge), a coherent theoretical framework with Lemmas/Theorems, a sound-and-complete algorithm, and consistent empirical improvements. The major weaknesses — imprecise F-PAG edge mark definitions and unclear experimental metric specification — are significant enough to prevent a higher score but do not invalidate the core contribution. The strengths (problem motivation, theoretical framework, algorithm, empirical results) are substantive enough to lift the paper above the 4.0-4.5 band where papers with comparable or greater theoretical issues sit. The paper sits most naturally alongside s0nYSwlV3I (5.0) in quality and contribution type, while falling clearly short of the 7.0 papers in polish and completeness.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
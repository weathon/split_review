---
job_id: 3fc22e79-26a6-499a-8aca-0bc94708247a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: TgLW2DiRDG.pdf
paper: Characterizing the Discrete Geometry of ReLU Networks
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, specifically learning theory, geometry/topology of neural networks, and interpretation of learned representations via the polyhedral structure of ReLU networks.

## Minimum Quality
Pass ✅ The paper contains the expected scientific components, including abstract, introduction, theoretical methodology/results, an algorithmic section, experiments, quantitative results, and discussion/limitations; while I have some concerns about proof exposition and empirical positioning, these do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect hidden instructions, suspicious prompts targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies the polyhedral complex induced by fully-connected ReLU networks through its connectivity graph, where nodes are linear regions and edges connect regions sharing a codimension-1 face. The main theoretical claims are an architecture-independent upper bound of \(2d\) on the average degree of the connectivity graph, a lower bound of \(\min(n_1,d)\) on the degree of every full-dimensional region, monotonicity and asymptotic tightness results for the average degree, and an upper bound on graph diameter of order \((m+1)^\ell\), independent of the input dimension \(d\). The paper also presents a BFS-based algorithm for enumerating regions and their adjacency structure, and empirical studies on synthetic and real datasets examining degree distributions, diameter behavior, and how data points are distributed across regions.

## Strengths
1. The central theoretical result is interesting and nontrivial. In particular, the claim in **Theorem 3.4** that the average degree of the connectivity graph is at most \(2d\), independent of width and depth, is a clean structural statement about ReLU region geometry that goes beyond the usual “count the number of regions” literature. If correct, this is a useful invariant-like constraint on the combinatorics of deep ReLU complexes.

2. The paper has a coherent geometric viewpoint throughout. The progression from regions, to bent hyperplanes, to the polyhedral complex, to the connectivity graph is well motivated. **Figure 1** does a good job introducing this ladder of abstractions: panel (b) makes the notion of neighboring regions concrete, panel (c) turns that into the graph object the theory studies, and panel (d) previews the degree-distribution perspective that later appears in experiments. This figure is not decorative, it genuinely carries the conceptual setup.

3. The formulation via sign sequences is useful and mostly well integrated into the arguments. The paper is strongest when it connects combinatorial properties of sign sequences to cell incidences. In particular, the interpretation on **Page 4** that edges in the connectivity graph correspond to sign sequences differing in one element is central and gives the theorems a clear combinatorial backbone.

4. The decomposition argument around removing a bent hyperplane is intuitive and is supported well visually. **Figure 3** is one of the stronger figures in the paper. The split between Category 1/2/3 cells helps the reader understand what **Lemma 3.2** and **Lemma 3.3** are trying to count, and panel (c) makes the graph-side effect of removing a BH much easier to parse. For a theory-heavy paper, this kind of visualization matters.

5. The paper does include nontrivial empirical validation rather than stopping at the theorem statements. The synthetic experiments in **Figure 4** and **Table 1** provide evidence that the average degree quickly approaches the \(2d\) upper bound as width/depth grow. The pattern in **Table 1** is fairly consistent: for \(d=4\), average degree rises from \(4.00\) to around \(7.85\), and for \(d=5\), from \(4.00\) to around \(9.80\), close to the theoretical ceilings \(8\) and \(10\) respectively. That alignment between theory and experiment strengthens the paper.

6. The paper is unusually clear about what is and is not tractable. The region-enumeration algorithm in **Section 4** is presented as an exact but expensive procedure, not as a scalable method solving the general extraction problem. That restraint is appreciated.

7. The empirical observation that data-containing regions tend to have higher connectivity is potentially useful. **Figure 6** makes this visible across MNIST, CIFAR10, and California Housing, and the paper does not overclaim causal interpretation. It is presented as an observation worth explaining, which is the right level of caution.

8. Presentation quality is strong overall. The notation is somewhat dense in places, but the narrative is easy to follow for a theory paper, and the paper is better organized than many submissions in this area.

## Weaknesses
1. The main theorem is stated broadly, but the proof sketch in the main paper leaves enough gaps that it is hard to fully verify from the paper itself. This matters because **Theorem 3.4** is the paper’s headline result. On **Pages 5–6**, the proof outline relies on induction jointly over number of BHs and dimension, together with the claim that \(h_i\) is itself a ReLU complex in dimension \(d-1\). That may be true under the cited assumptions, but in the main paper the justification is compressed to the point where the burden is shifted to the appendix and prior work. In particular, the transition from the inductive inequalities to the final bound depends critically on treating \(h_i\) as an object to which the lower-dimensional induction hypothesis applies. Since the theorem’s scope is “all fully-connected ReLU networks” almost everywhere, this step deserves a more explicit argument in the main text, not only a sketch.

2. The generalization from the \(k=d\) case to all \(k\)-cells in **Theorem 3.1** is too quick in the main paper. On **Page 6**, the argument says one can restrict to subcomplexes given by fixing \(d-k\) zeros and then apply the same reasoning. But this reduction is doing substantial work. It requires that these restricted intersections are indeed valid \(k\)-dimensional ReLU subcomplexes with the same incidence structure assumptions needed by the proof. As written, the theorem reads stronger than the amount of justification provided in the main paper. This is not a request for “more theory for theory’s sake”; it matters because the result is presented as a theorem for all \(k\), not merely a corollary with obvious reduction.

3. The diameter upper bound in **Theorem 3.8** is the weakest theoretical component. The proof sketch on **Page 20** is intuitive but not fully convincing as stated. The recursive argument informally says that inside each first-layer region, one can cross each second-layer hyperplane at most once, and then continue recursively, leading to \(\prod_j (m_j+1)\). However, bent hyperplanes are not ordinary hyperplanes globally, and the argument needs a careful statement about how local traversals compose without re-crossing previously handled BH segments when moving across adjacent first-layer regions. Right now the proof reads more like a plausible recursion than a tight graph-theoretic derivation. Since the abstract and contributions list elevate the diameter result alongside the degree bound, I expected a more watertight treatment in the main text.

4. The algorithm section is underspecified in ways that affect reproducibility and confidence in the experiments. In **Algorithm 1** on **Page 7**, line 6 uses
\[
\text{SOLVELP}(-\Phi_{s_i}, \Phi_s, \beta_s + e_i)\ge \beta_{s_i},
\]
but the notation here is not sufficiently precise. It is unclear whether \(\text{SOLVELP}\) returns the optimal objective value, the optimizer \(x^\*\), or something else. The surrounding prose later describes checking whether the optimal solution violates the original inequality, which suggests a condition involving \(\Phi_{s_i}^\top x^\* + \beta_{s_i} > 0\), but the pseudocode as written does not match that description cleanly. Also, line 5 iterates “for \(i\in \{0,\ldots,n\}\)”, which appears off by one given neuron indexing elsewhere. This is not a cosmetic complaint; if the core enumeration procedure is ambiguous, then the empirical pipeline becomes harder to trust.

5. The derivation of the half-space system in **Section 4**, especially **Equations (2) and (3)** shown on **Page 7**, is not explained enough for a reader to independently verify correctness. The use of \(\mathrm{diag}(s^{(j)})\), \(\mathrm{diag}(\mathrm{ReLU}(s^{(j-1)}))\), and the recursive propagation of \(\Phi^{(j-1)}\) and \(\beta^{(j-1)}\) is suggestive, but several details are implicit. For example, if \(s^{(j-1)}\in\{-1,1\}^{m_{j-1}}\) for \(d\)-cells, then \(\mathrm{ReLU}(s^{(j-1)})\) acts as a binary mask, but this should be stated explicitly and related to the affine map restricted to a region. Also, the dimensions of the matrices and vectors are not obvious from the displayed equations. Since these formulas are the backbone of the LP-based enumeration, they need clearer exposition.

6. The empirical section supports the main qualitative story, but it is thin on comparative context and uncertainty analysis. For example, **Figure 5** compares estimated diameter to the theoretical upper bound, yet the plotted relationship is descriptive only. There is no direct quantitative assessment of how loose the bound is as a function of \(m,\ell,d\), nor any analysis of whether the apparent logarithmic trend is robust beyond the tested range. Similarly, **Table 1** reports diameter estimates obtained by midpoint between upper/lower graph-diameter bounds from another algorithm, but the uncertainty introduced by using estimated rather than exact diameters is not reflected in the conclusions beyond a brief note. Since one of the paper’s notable claims is that diameter behaves almost independently of input dimension, more care is needed here.

7. The real-data experiments are interesting but scientifically limited by partial enumeration. On **Page 9**, for CIFAR10 and California Housing the search is terminated after traversing 8 million polyhedra, then augmented with polyhedra containing 10,000 sampled training points. This procedure is understandable computationally, but it introduces a strong sampling bias toward accessible regions and data-containing regions. As a result, statements like “Across all datasets, the neighbor counts for polyhedra containing training data tend to be higher than the upper bound for the average neighbor count of all polyhedra” are difficult to interpret rigorously, because the “all polyhedra” distribution is exact for MNIST but truncated for CIFAR10 and California Housing. This affects the strength of the empirical claims in **Figure 6** and **Figure 7**.

8. The novelty relative to adjacent graph-based viewpoints on ReLU region geometry could be positioned more sharply. The paper does cite recent work using connectivity graphs and transition graphs, but the distinction is not always crisp enough. On **Page 2**, the paper says recent work has analyzed the connectivity graph to characterize VC-dimension and region volumes, and then presents its own bounds. I would have liked a more explicit table or paragraph separating what is already known for hyperplane arrangements, what was known under architectural restrictions, and what exactly is first established here under the current assumptions. Without that, the reader has to do some work to determine how much of the contribution is a deep-network extension versus a reframing of known combinatorial geometry.

9. Some experimental choices are under-motivated from the perspective of the paper’s stated goals. The synthetic tasks are based on clustering problems from three isotropic Gaussians, but the theoretical results are architecture-level and largely weight-generic. It is not obvious why training on this particular family of tasks is the right lens for validating the geometric phenomena, as opposed to evaluating random networks directly under the genericity assumptions. Because of this, it is hard to separate properties induced by the architecture from properties induced by optimization and data. The paper partly acknowledges this, but the experimental design still mixes several factors.

10. A number of claims in the discussion are intriguing but speculative. For instance, the argument on **Page 10** that classification may leave data on more unbounded regions whereas regression tends to place data on bounded regions is plausible, but nothing in the paper establishes this mechanism beyond a small number of examples. This is fine as hypothesis generation, but the writing occasionally edges close to interpretation that the experiments do not yet support.

## Questions
1. For **Theorem 3.4** and the use of induction through **Lemma 3.3**, can the authors make explicit in the rebuttal which exact property guarantees that \(h_i\) is a valid \((d-1)\)-dimensional ReLU subcomplex to which the induction hypothesis applies? A short, self-contained explanation here would substantially increase my confidence in the proof.

2. For **Theorem 3.1**, can the authors clarify the reduction from \(d\)-cells to general \(k\)-cells more explicitly? In particular, when restricting to the intersection of \(d-k\) BHs, what assumptions ensure the resulting object preserves the needed genericity/supertransversality properties and incidence structure?

3. For **Theorem 3.8**, can the authors provide a more formal version of the recursive path argument? I am specifically unsure why the concatenation of layerwise traversals cannot force repeated crossings of BH segments that would violate the claimed upper bound.

4. Please clarify the exact semantics of **Algorithm 1**, line 6. Does \(\text{SOLVELP}\) return \(x^\*\), the optimal objective value, or a boolean redundancy test? As written, the pseudocode and the prose description are not fully aligned. A cleaned-up mathematical statement of the LP, including objective and feasibility conditions, would help.

5. For **Equations (2) and (3)**, please add dimensions and a brief derivation. Right now the formulas are plausible, but not transparent enough for an informed reader to rederive or implement without consulting outside material.

6. Regarding the experiments in **Figure 6** and **Figure 7**, how sensitive are the conclusions to the 8-million-region truncation used for CIFAR10 and California Housing? Even a simple analysis showing stability with respect to smaller cutoffs, or reporting what fraction of sampled training points fell outside the initially enumerated set, would make these observations much more convincing.

7. Did the authors examine random networks, not only trained ones, to disentangle generic architectural behavior from training-induced behavior? Since the main theorems are almost-everywhere statements over weights, this comparison seems highly relevant and could strengthen the empirical narrative.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns beyond standard computational cost considerations. The paper mainly studies theoretical and geometric properties of fully-connected ReLU networks and does not raise obvious issues related to privacy, fairness, safety, or human subjects.

## Soundness Rating
3: good. The core arguments appear plausible and the empirical evidence is consistent with the claims, but some of the most important proofs, especially the general \(k\)-cell extension and the diameter upper bound, are not fully convincing from the main paper alone.

## Presentation Rating
4: excellent. The paper is well organized, the narrative arc is clear, and several figures, especially **Figures 1** and **3**, materially improve understanding. The main presentation issue is localized mathematical underspecification in **Section 4** and parts of **Section 3**.

## Contribution Rating
3: good. The average-degree result is a meaningful contribution to understanding ReLU region geometry, and the connectivity-graph perspective is worthwhile. I am somewhat less convinced by the strength of the diameter result and by the practical implications of the experimental observations, which keeps this from the top tier for me.

## Overall Rating
8: Accept, good paper (poster). This is a strong theory paper with an interesting central result, solid exposition, and supportive experiments. I do have real concerns about proof exposition and the precision of the algorithmic section, but on balance the paper makes a valuable contribution that ICLR readers interested in geometry/topology of neural networks would benefit from seeing.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the surrounding literature on ReLU region geometry, though I did not fully formal-verify every proof detail.
- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5, 3
Now I have a complete picture of the paper. Let me formulate the consolidated review.

## Summary

This paper studies the problem of $k$-means clustering of segments in $\mathbb{R}^d$, where the distance between a center and a segment is the integral of Euclidean distances over all points on the segment. It proposes an $\varepsilon$-coreset construction that reduces this problem to weighted point clustering, claiming $O(\log^2 n)$ coreset size and $O(nd)$ computation time for constant $k,\varepsilon$. The paper includes definitions, a theoretical setup, and an experimental evaluation on synthetic and real datasets (motion vectors, road networks).

## Strengths

- **Novel and well-motivated problem formulation.** The paper identifies an underexplored variant of $k$-means where the input consists of continuous segments rather than discrete points, with the distance defined via an integral over each segment. This is a natural extension for applications such as motion vector analysis in video (line 180) and road network center-finding (lines 182–183), and differs from prior work on infinite-line clustering (Marom & Feldman, 2019).

- **Principled reduction approach.** The core idea — converting segment clustering to weighted point clustering via a coreset — is conceptually clean and enables the use of standard point $k$-means algorithms (Arthur & Vassilvitskii, 2007) off the shelf, as described in Section 1.3 (lines 55–56). This bridges continuous-object and discrete-point clustering in a provable way.

- **Multiple real-world and synthetic datasets.** The experiments (Section 3) use three distinct data sources: synthetic segments in $\mathbb{R}^{10}$, real motion vectors from video, and road segments from OpenStreetMap (Malaysia/Singapore/Brunei and southern Italy). The paper also varies the segment count $\{100i\}_{i=2}^{10}$ and repeats experiments 40 times (lines 186–188), showing a systematic attempt at evaluation.

- **Open-source code.** The paper states that an open-source implementation is available (line 166), which supports reproducibility.

## Weaknesses

### Fatal
None.

### Major

- **Experimental results are reported only qualitatively, with no numerical evidence.** The results section (lines 190–192) states that OUR and OPT produced "essentially identical results" with "significantly lower time for OUR," and that LINE-CLUSTERING gave "noticeably worse results in noticeably higher running time." No numerical tables or approximation ratios are reported — no loss values, no runtime measurements in seconds, no variance statistics beyond percentile bounds mentioned for Figure 3. The reader cannot assess the magnitude of approximation error, the actual runtime speedup, or the statistical significance of the results. For a paper whose central claims are empirical as well as theoretical, this level of reporting is insufficient to support the conclusions.

- **The experiments do not validate the claimed $O(\log^2 n)$ coreset size.** The abstract claims coreset size $O(\log^2 n)$ for constant $k,\varepsilon$, yet the experiments fix the coreset per segment at $|P_\ell| = 10$ regardless of the number of segments $n$ (line 170). There is no experiment that varies $n$ and measures how the coreset size grows, nor any justification for why a fixed size of 10 suffices for the values of $n$ and $\varepsilon$ tested. This creates a disconnect between the theoretical size bound and the empirical setup.

- **The LINE-CLUSTERING baseline solves a different problem.** The paper explicitly acknowledges (line 173) that LINE-CLUSTERING fits centers to infinite lines, not segments. This baseline is therefore expected to perform poorly on segment data, making the comparison largely uninformative. A more meaningful baseline would be a direct segment-clustering method (e.g., dense sampling of points on each segment and then running $k$-means on those points, which is essentially what OPT does with 1,000 points per segment).

- **No runtime scaling analysis.** The paper claims "significantly lower time for OUR" (line 192) and that running time is "mostly dominated by the call to the $k$-means computation" (line 192), but reports no actual runtime numbers, no scaling with $n$, and no comparison of wall-clock time. The claimed computational advantage cannot be verified or quantified.

### Minor

- **Only $k=2$ is tested.** The experiments use $k=2$ centers, described as "chosen arbitrarily" (line 168). The general method is defined for any $k$, but there is no evidence that the approach works for larger values.

- **The ground-truth loss approximation uses an arbitrary 10,000 points per segment.** The "Loss" evaluation method (line 174) uses $|P_\ell| = 10,\!000$ points per segment as a high-resolution approximation of the true integral loss. The choice of 10,000 is not justified, and there is no ablation showing that results are stable with respect to this parameter.

- **No comparison against a simple discrete baseline.** A natural and straightforward baseline would be to uniformly sample a fixed number of points from each segment and run $k$-means++ on the resulting point set. The paper compares against OPT (1,000 points per segment) and LINE-CLUSTERING, but not against this simpler alternative, which would help isolate the value of the coreset construction itself.

### Trivial
None.

## Nice-to-Haves
- Include a baseline that directly samples points on segments and clusters them using $k$-means++ (without coreset weighting), to isolate the benefit of the coreset construction.
- Add a brief ablation study varying $|P_\ell|$ (e.g., 5, 10, 20, 50) to show how approximation quality changes with coreset size.
- Provide a more complete discussion of how the coreset construction parameterizes $\varepsilon$ and $\delta$, and how these are set in experiments.

## Removed Points

These points were raised by the reviewers but are excluded from the main evaluation for the following reasons:

1. **"The core theoretical contribution (Algorithm 1, Algorithm 2, Theorem 2.9) is not presented"** — The extracted text does not contain the algorithms or Theorem 2.9 (Section 2.2 consists of a single sentence, and the paper jumps to Section 3). However, per the instructions, content that the parser cannot extract (e.g., pseudocode in figures, theorems in special formatting) is a formatting artifact, not an author error. The original submission is assumed to contain this material.

2. **"Figure 3 is missing"** — The results figure is referenced at line 190 but not present in the extracted text. This is a parser artifact.

3. **"Section G (video tracking application) is missing"** — The appendix content was stripped by the parser, which is standard and expected.

4. **"The paper has typos, formatting issues"** — These are parser artifacts and are not present in the original submission.

5. **"The empirical evaluation cannot salvage the missing theory"** — The portion about "missing theory" is removed per point 1 above. However, the criticism about thin empirical evaluation is retained in the Major weaknesses section.

6. **Strength Finder claim: "First provable ε-coreset for segment clustering"** — This is stated as a contribution but is not a "strength" that can be evaluated from the available text; it is a claim that depends on content (the algorithm and theorem) that was not extractable. I treat it as a stated contribution but not as an independently verifiable strength.

7. **Strength Finder claim: "Small coreset size with efficient computation"** — Similar to point 6; the abstract claims this, but the experiments use fixed size $|P_\ell|=10$ without validating the $O(\log^2 n)$ scaling.

8. **Strength Finder claim: "Empirical validation of approximation quality"** — The paper's experimental reporting is too qualitative for this to be considered a strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report numerical results.** Provide a table with median approximation ratios (OUR/OPT) and their 25th/75th percentiles for each dataset and each $n$, along with wall-clock runtime in seconds. Without numbers, the empirical claims are unverifiable.

2. **Validate the coreset size bound empirically.** Vary $|P_\ell|$ (e.g., from 5 to 100) and measure the resulting approximation error, or vary $n$ and show that the coreset size needed to maintain a fixed error grows sublinearly.

3. **Replace or augment the LINE-CLUSTERING baseline.** Use a simple dense-sampling baseline (e.g., 100 uniformly sampled points per segment → $k$-means++) to provide a fair comparison, in addition to or instead of LINE-CLUSTERING.

4. **Report actual runtime numbers** as a function of $n$, showing the scaling behavior and where the time is spent.

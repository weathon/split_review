---
job_id: 1c589a33-74f7-4711-882e-ddf0a27d4553
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: QryPmx2MNh.pdf
paper: Chain of Thought in Order: Discovering Learning-Friendly Orders for Arithmetic
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies Transformer learning dynamics, sequence ordering, optimization over permutations, and arithmetic reasoning as a machine learning problem.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion; while I found several methodological and presentation weaknesses, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-directed instructions, or obvious manipulation attempts in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies a new problem, discovering a learning-friendly order of decoder target tokens for Transformer training on arithmetic tasks. The proposed approach ranks candidate permutations using early-stage validation loss after short training on a mixture of reordered targets, and extends this idea with a hierarchical global-local search to handle large permutation spaces. Experiments on three synthetic order-sensitive arithmetic tasks and one multiplication task show that the method can often recover a favorable order, including rediscovering the least-significant-digit-first order for multiplication.

## Strengths
The paper asks a clean and interesting question that is easy to overlook: not only which intermediate reasoning steps to include, but also in what order they should be generated. That is a meaningful angle on chain-of-thought style supervision, especially for autoregressive models where causality and token order are inseparable.

I appreciated that the paper does not merely claim “order matters”, it attempts to automate order discovery. The core heuristic, using early-stage loss profiling across a mixture of permutations, is simple and operational. Even if one ultimately disagrees with some of the framing, this is a concrete search procedure rather than a vague intuition.

The synthetic tasks are constructed to be order-sensitive in a fairly transparent way. In Section 5.1, the recurrences for ReLU, Square-19, and Index make it clear why the forward order should be easier: each next token is naturally computed from previously generated ones, while reverse or random orders destroy that causal structure. This makes the experiments interpretable.

The main empirical story is easy to follow. **Table 1** provides a clear sanity check that the proposed tasks indeed separate friendly and unfriendly orders, with forward order near-perfect on most settings and reverse order near zero. This is important because the whole search method depends on there being a real learnability gap across permutations.

I also found **Figure 5(a)** useful. It directly visualizes the central premise of the method, namely that the favorable permutation obtains lower validation loss after short training than unfavorable ones. That figure does more work than the prose here, because it shows the separation across many candidate permutations rather than only reporting final success after full retraining. Likewise, **Figure 5(b)** is a good attempt to connect the proxy signal to downstream usefulness, at least for ReLU and Square-19.

The hierarchical search is intuitively motivated. **Figure 4** helps clarify the intended global-then-local workflow, where block-level search first identifies coarse structure and local refinement then reorders within blocks. Given the factorial search space, some structured decomposition is necessary, and the high-level idea is reasonable.

The negative example around soft permutation optimization is also valuable. **Figure 2(a)** and **Figure 2(b)** support the authors’ argument that naïve soft permutation learning leaks future information and yields misleadingly low loss. The visual in **Figure 2(b)**, with nonzero mass around off-diagonal entries, is a concrete demonstration of the issue rather than just a speculative concern.

Finally, the multiplication experiment gives one non-synthetic touchpoint beyond the authors’ custom tasks. Rediscovering the known least-significant-digit-first order is a sensible validation target for the search procedure.

## Weaknesses
1. **The empirical scope is too narrow to support the broader framing around “unraveling chain of thought” or improved reasoning ability.**  
   The title, abstract, and conclusion position the work as discovering learning-friendly chain-of-thought orders for Transformers, but almost all evidence is limited to carefully designed arithmetic recurrences where the correct order is essentially baked into the task definition. In Section 5.1, the three main tasks are explicitly constructed so that the forward recurrence is easy and other permutations are difficult. This makes them useful toy problems, but also weak evidence for the broader claim that the method “unravels” chain of thought in a meaningful sense. The only non-toy task is multiplication, and even there the result is rediscovering a previously known order rather than establishing usefulness on a new reasoning setting. As written, the paper is closer to a proof-of-concept on synthetic order-sensitive recurrences than a general method for chain-of-thought discovery. That distinction matters because the current framing overstates the significance.

2. **The search procedure is not compared against enough serious baselines in the main paper.**  
   The proposed method is, at heart, a search strategy over permutations using a proxy objective. For such a paper, baseline choice is crucial. In the main paper, the comparison is mostly against forward, reverse, and random orders, plus a short discussion of failed soft-permutation optimization. That is not enough to establish that the proposed search is the right tool. The appendix mentions an evolutionary strategy baseline, but the main-paper evaluation does not include a direct head-to-head comparison between the proposed hierarchical search and alternative search methods under comparable compute budgets. This is especially problematic because the claimed contribution is algorithmic efficiency in exploring huge permutation spaces. If the key claim is “our method efficiently finds good orders”, then comparisons to random search, beam-like local search, greedy swap search, or evolutionary search belong in the main paper, not relegated away. Without this, it is hard to tell whether the gains come from the specific loss profiling idea or simply from exploring a structured search space with enough compute.

3. **There is a validation protocol issue: the same held-out split appears to serve both as model-selection signal for permutation search and as the reported evaluation set.**  
   Section 4 defines \(D'\) as a validation set used to rank permutations via Equation (4.1). Section 5.2 then states that there is a training set and an “evaluation set” of 1,000 samples, and the success rate is reported on the evaluation set. The paper does not clearly separate a validation set used for search from a test set used only for final reporting. If the same split is used both to choose the permutation and to report the final success of the discovered permutation, then the evaluation is optimistic because the order-selection process is tuned to that split. This matters a lot for a search-heavy paper: when one searches over many permutations, reusing the same held-out set for final reporting can substantially inflate results. A clean train/validation/test separation is needed here.

4. **The method description is underspecified and mathematically inconsistent in several places, which makes the search procedure hard to verify or reproduce from the main paper alone.**  
   There are multiple notation and indexing problems in Section 4:
   - In **Equation (4.2)**, the \(Q_i\) are described as block-level permutations, but they are typed as \(Q_i \in [0,1]^{L\times L}\) rather than permutation matrices. If these are true permutations, they should be discrete matrices in \(\{0,1\}^{L\times L}\) with one 1 per row and column; if they are soft block operators, then the leakage problem discussed earlier reappears.
   - In the **Local stage** on Page 5, the text says “Let \(P_1 \in P_g\) be the initial permutation”, which is not type-consistent. \(P_g\) is introduced as a single permutation, not a set, so this should presumably be “Let \(P_1 := P_g\)” or similar.
   - The set of block lengths is written as \(l = \{2, 3, \ldots, \lfloor L/2 \rfloor\}^{2}\), which appears malformed.
   - In **Equation (4.4)**, the number of “block-reordering candidates” is given as \(\lfloor L/l \rfloor\), but if one is truly reordering blocks, the natural count would typically be factorial in the number of blocks, not linear. So either the search is restricted to a very special subset of block reorderings, or the notation is inaccurate. As written, it is not clear what candidates are actually evaluated.
   
   These are not cosmetic issues. This paper’s contribution is an algorithmic search method, so ambiguity in the search space and candidate generation directly affects scientific assessability.

5. **The central optimization objective is not aligned with some of the broader claims made in the paper.**  
   In **Equation (3.2)**, the target permutation \(\pi\) is selected to minimize the expected loss on the *permuted* target sequence, \(\ell(\mathcal{T}_{\theta^\pi_{\mathrm{ERM}}}, X, \pi(Y))\). That is fine if the goal is simply to find a target representation that is easier to learn. However, the abstract and conclusion repeatedly suggest that the method improves arithmetic reasoning and generalization more broadly. Those stronger claims would require showing how training on \(\pi(Y)\) translates into better performance on the original task under a fixed canonical output representation, or at least explaining why the permutation itself should be considered part of the task definition rather than a change in label space. Right now the paper mixes two notions: “finding an easier representation of the same task” and “improving reasoning ability.” Those are not the same thing.

6. **The evidence that early loss is a reliable proxy for eventual trainability is suggestive, but still too weak.**  
   **Figure 5(b)** is the main support for the idea that permutations ranked highly by early validation loss are truly better. But the evidence is partial: the plot only includes retraining on the top 32 orders and omits the hardest task, Index, because success rates are near zero. The paper then argues that the top-ranked order is still useful because it is the forward order “by construction”. This is circular. For the hardest setting, the proxy is not shown to predict practical success. More generally, a stronger paper would quantify the rank correlation between early loss and final success, perhaps across all or many permutations for smaller \(L\), rather than relying mainly on one illustrative figure.

7. **Several headline claims are stronger than what the experiments actually show.**  
   For example, the abstract claims the method identifies a learning-friendly order out of “a few billion candidates”, and Section 5.5 repeats that it identifies a single solution among roughly \(13! \approx 6 \times 10^9\) possibilities. But the method does not evaluate a substantial fraction of that space; it explores a restricted hierarchical candidate family and succeeds on these tasks. That is still interesting, but it is not the same as demonstrating robust identification over the full permutation space. Likewise, the claim in the conclusion that the method “markedly enhances a Transformer's reasoning ability” goes beyond the evidence, which is mainly about target-order representation effects in arithmetic toy tasks.

8. **The multiplication experiment is too limited to carry much weight.**  
   The paper emphasizes recovering the reverse-digit order known from prior work, but **Table 2** only reports PROD at \(L=10\), and there is no broader benchmark table for multiplication across operand lengths comparable to **Figure 1**. This makes the multiplication result feel more like a spot check than a convincing experimental pillar. Since multiplication is the one task with direct relevance to prior literature and a less hand-crafted structure than the synthetic recurrences, it deserved more substantial treatment.

9. **Presentation quality is mixed, and some figures/tables expose unresolved interpretation issues.**  
   **Figure 6(a)** and **Figure 6(b)** aim to summarize the success of discovered orders under different initializations, but they are not as informative as they could be. The curves compare forward, reverse, and discovered orders, yet the search budget and failure cases are not made explicit in the figure itself. More importantly, **Table 2** reveals that the discovered final order is not always the true forward order, for example Square-19 at \(L=8\) and \(L=13\), and Index at \(d=4,8\). The text sometimes interprets this as success because the found order is still “learning-friendly”, but the criterion for success then becomes blurry. Is the goal exact recovery of the optimal order, recovery of any sufficiently good order, or merely improvement over reverse? The paper slides among these notions. A more careful definition of success, reflected consistently across text, figures, and tables, is needed.

10. **The paper is under-positioned relative to adjacent literature on output formatting/order in arithmetic and CoT structure.**  
   The related work cites Shen et al. (2023) and several arithmetic/CoT papers, but the positioning still feels incomplete. There is relevant recent work studying how decoding order, output representation, or explicit algorithmic intermediate formats affect arithmetic learnability in Transformers. Since the present paper’s core contribution is about automatically selecting output order, it should do a better job distinguishing itself from prior studies that already show strong order or representation effects, beyond saying that those orders were chosen heuristically. The novelty is not in discovering that order matters, it is in the search procedure, and that distinction should be sharpened.

## Questions
1. Please clarify the data split protocol. Is the same 1,000-sample “evaluation set” in Section 5.2 used both for permutation ranking in Equation (4.1) and for final success-rate reporting? If yes, I would view that as a significant evaluation problem. A separate validation set for search and untouched test set for final reporting would materially increase my confidence.

2. Can the authors provide a precise, implementation-level description of the candidate generation in the hierarchical search? In particular:
   - In **Equation (4.2)**, are the \(Q_i\) hard permutation matrices or soft block operators?
   - In **Equation (4.4)**, why are there only \(\lfloor L/l \rfloor\) block-reordering candidates instead of all \((\lfloor L/l \rfloor)!\) permutations of blocks?
   - What exactly is the search neighborhood at each local-stage step?
   Clarifying this would help assess whether the method is principled or largely heuristic.

3. For small \(L\), where exhaustive enumeration is feasible, can the authors report the rank correlation between early validation loss after loss profiling and final success after full training across *all* permutations? That would be a much stronger validation of the central proxy assumption than the current partial evidence in **Figure 5**.

4. The paper often treats “recovered the forward order” and “found a learning-friendly order” as almost interchangeable, but **Table 2** shows several cases where the final order is not the canonical forward order. Are these alternative orders genuinely near-optimal under full retraining? A table with final success rate for the discovered order versus the true forward order for every row in **Table 2** would make the claims much clearer.

5. Since the contribution is a search algorithm, why are more search baselines absent from the main paper? I would especially like to see a comparison, under matched compute budget, to random search and a simple greedy local-swap or beam-search baseline. If such results exist and show a real advantage, they could strengthen the paper substantially.

6. For the multiplication task, can the authors expand beyond the single \(L=10\) setting in **Table 2** and show whether the discovered order consistently scales across operand lengths, ideally in a format similar to **Figure 1**? Right now the multiplication evidence is too thin to weigh heavily.

7. The paper claims that using a small Transformer for exploration is sufficient because “the learning-friendly orders must be universal” (Page 5). What empirical evidence supports this universality assumption? A direct comparison of order rankings induced by small versus large models would be helpful.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are evident from the paper itself. The work studies synthetic arithmetic tasks and Transformer training behavior, without involving human subjects, sensitive personal data, or obviously harmful deployment claims.

## Soundness Rating
2: fair. The core empirical observations are plausible and some results are convincing, but the evaluation protocol, baseline coverage, and algorithmic specification are not strong enough for a higher soundness score.

## Presentation Rating
2: fair. The paper is readable at a high level, but several equations and search steps are underspecified or inconsistent, and some claims are framed more broadly than the evidence supports.

## Contribution Rating
2: fair. The problem is interesting and the loss-profiling heuristic is potentially useful, but the current evidence is too limited and synthetic to justify a stronger assessment of overall contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
Interesting idea and a decent proof-of-concept, but the current version falls short of ICLR standards due to limited empirical scope, insufficient baseline comparisons, unclear search specification, and a problematic validation/evaluation split.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. The core ideas and experiments are within my expertise, and I checked the main equations, figures, and tables carefully.
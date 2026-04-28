# Node Similarities under Random Projections: Limits and Pathological Cases

- Decision: Accept
- Avg Score: 5.80
- Scores: 8, 6, 6, 6, 3

## Abstract
Random Projections have been widely used to generate embeddings for various graph learning tasks due to their computational efficiency. The majority of applications have been justified through the Johnson-Lindenstrauss Lemma. In this paper, we take a step further and investigate how well dot product and cosine similarity are preserved by random projections when these are applied over the rows of the graph matrix. Our analysis provides new asymptotic and finite-sample results, identifies pathological cases, and tests them with numerical experiments. We specialize our fundamental results to a ranking application by computing the probability of random projections flipping the node ordering induced by their embeddings. We find that, depending on the degree distribution, the method produces especially unreliable embeddings for the dot product, regardless of whether the adjacency or the normalized transition matrix is used. With respect to the statistical noise introduced by random projections, we show that cosine similarity produces remarkably more precise approximations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper focuses on the practice of using random projections (RP) to learn graph embeddings. In particular, they motivate the advantage of using Cosine Similarity over Euclidean Distance (which is widely popular), grounded in theoretical evidence. The authors show that a nodes with low/high degree enjoy weaker guarantees under Euclidean-based RP. They further extend their scope to the ranking context, where they build upon the general setting results and conclude that Cosine Similarity-based RP yield more robust rankings.

### Strengths
The paper studies an important and (much to the author's credits) well-motivated problem: random projection (RP) for dimensionality reduction on large-scale graph representation learning. Given the prevalence of RP and JL Lemma under many graph representation learning methods today, I believe their analysis on a fundamental design choice (Euclidean vs. Cosine Similarity) will be of great influence to the community. In particular, the theoretical question of how node degree affects graph representation learning is one with clear motivation --- given the influence highly-connected nodes have in many real-world applications. As such, I believe both their theoretical results and techniques will be of interest to the community broadly. Overall, the paper is very clearly written and the narrative is centered.

### Weaknesses
For Figure 1, it may be helpful to the audience if the axis and legends are accompanied by a text description as opposed to just the (paper-defined) mathematical notations. For example, it would help clarity if the blue dots are clearly labeled "Cosine" and the y-axis states "node degree".

In the theoretical sections, the presentation of the theorems and their accompanied analysis is helpful for interpreting the theorems. However, I felt that the contrast between results in Section 2.1 and 2.2 can be made stronger (or a subsection itself). See Q2 in the questions section for an example. 

For the experimental section, I feel that including simple experiments independent of the ranking application can better support the theoretical analysis in Section 2. For example, would it be possible to design a simple example (synthetic network) where the two different RPs generate substantially different results for a high-degree node? This could also be in the form of a written example.

### Questions
1. Can the authors clarify, in simple terms, what difference between the Euclidean and Cosine dissimilarity led to one generating substantially poorer guarantees for high-degree nodes --- based on the theorems? 

2. What is the approximate three-sigma interval, and how is it relevant? I see that the "interval endpoints do not depend on the node degrees" in the cosine case, but it is unclear to me the relationship between this interval and the projected features/learned embeddings. I think it will be helpful to not only highlight this distinction (as the authors have by italicizing), but also motivate it in the broader context clearly.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates how well dot product and cosine similarity are preserved by random projections when these are applied over the rows of the graph matrix, concluding that the variance of the dot product estimation is worse than cosine similarity estimation.

### Strengths
1. Each mathematical description is carefully written. 
2. The specific theoretical results, Theorems 2.2 and 2.5 are novel, as far as I know. They successfully associate the variance in estimating relevance (dot product or cosine similarity) with the graph structure.

### Weaknesses
1. Johnson-Lindenstrauss Lemma is roughly stated in Line 118 without the reference for proof, but not formally introduced as a Theorem. As there are some variants in the statement, it is essential to specify which form to consider with specific reference with proof.
2. The further discussion associating JL Lemma and Theorem 2.2. would be preferable. What aspects of JL Lemma previous researchers have tended to miss and what aspects of the problem setting lead to a higher variance in estimation? Would it not be possible to give an intuitive explanation so readers can understand it without reading the proof of Theorem 2.2?
3. While each theorem in this paper is interesting, the direction of the whole discussion is not justified by those theorems.
Specifically, in Conclusion section, the Authors states that "we propose that practitioners of random projection methods first use the embeddings $u \mapsto \frac{X_{u*}}{\|X_{u*}\|}". However, easiness in estimating an index (in this case, a similarity measure) does not directly mean we can recommend it. Rather, such a measure is problem-dependent. We cannot choose a similarity measure arbitrarily even if we know one is easy to estimate than another. For example, if we set $\mathrm{rel}_{uv} = 1$, which is a constant function, then we can trivially estimate it from any random projection (we can ignore the projection and simply always output 1). Nevertheless, this relevance measure would not be useful in real applications. If we propose to use cosine similarity, we need to discuss its meaning from a graph perspective, also.
4. Related to the above, the Authors should have discussed the difficulty of the estimation problem itself. The reason why a trivial algorithm can estimate the above trivial similarity measure $\mathrm{rel}_{uv} = 1$ is that the similarity measure estimation problem itself is easy as the variance of the true similarity $\mathrm{rel}_{uv}$ is zero (here, variance is defined when we sample $u$ and $v$ randomly), not that the trivial algorithm is excellent. Likewise, the Authors should have discussed the difference between the difficulties in the dot product similarity and cosine similarity. In this sense, Proposition 3.2 and 3.6 are partially helpful but not sufficient, as $\mathrm{rel}_{uv} = 10000$ is still an easy problem, while the upper bound of the value is large. One could evaluate the variance of $\mathrm{rel}_{uv}$ for both the dot-product case and cosine case, showing its dependency on the graph structure. If the problem difficulties are almost the same but the estimation performance through the random projection is much worse for dot-product than for cosine similarity, it is worth alerting. However, if the variance of $\mathrm{rel}_{uv}$ is higher for dot-product case, which means that the estimation problem itself is more difficult, then your comparison between Theorems 2.2 and 2.5 may not be practically meaningful.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors investigate random projections (RP) for graph matrices, specifically adjacency and transition matrices, to produce 'low-dimensional' node embeddings. They derive both asymptotic and finite-sample results in the spirit of the Johnson-Lindenstrauss (JL) lemma, assessing the distortion of two node similarity measures—dot products and cosine similarities—under Gaussian random projections. The authors demonstrate that RP can significantly distort dot product similarity, with the extent depending on the degrees of the nodes involved. In contrast, cosine similarity proves more robust, exhibiting less distortion under RP. They apply these findings to a ranking problem, theoretically establishing that normalized discounted cumulative gain (NDCG) is more stable when cosine similarity is used as the similarity measure compared to dot product similarity. Finally, the authors provide numerical evidence supporting their theoretical claims using a real-world dataset.

### Strengths
The main strengths, in my opinion, are:

1. **Relevance**: Node embedding is highly relevant within graph machine learning and representation learning, and RP offer a promising approach to obtaining these embeddings. The study focuses on well-established similarity measures widely used in practice, and the application to ranking is equally pertinent.

2. **Rigorous Mathematical Treatment**: The paper is technically sound, with proofs that appear correct and rigorous.

3. **Clear Presentation**: The paper is well-written and easy to follow, aside from a few issues outlined below.

### Weaknesses
1- **Claims of Novelty and Improvements upon Known Results**: To clarify, I do consider the paper to make a valid contribution with its theoretical analysis of random projections (RP) for node embeddings and the resulting distortions in well-known similarity measures. However, it is sometimes challenging to determine which results the authors claim as novel. It would be helpful if the authors clearly delineate what they consider to be novel contributions versus extensions or refinements of existing work. For instance, in the introduction, Section 2, and the appendix, the authors appear to suggest that their rotation argument—which follows directly from well-known properties of Gaussian distributions—constitutes a novel contribution. They state that "we use the rotation argument to provide a new representation for the dot product and cosine similarity under random projections." However, if I understand correctly, the dot product representation could be derived using the distribution of the off-diagonal entries of a Wishart matrix, with a correlation coefficient corresponding to their parameter $\rho$. 

The inclusion of detailed proofs in the appendix is appreciated for self-containment, but much of the content presented there either derives from well-established results or can be directly obtained through known concentration or asymptotic arguments. If my interpretation is accurate, the paper’s genuine technical novelty lies in the more refined bounding of relevant quantities following classical concentration or asymptotic approaches. This does sometimes lead to improved results, but in certain sections, such as Section A.III.5, the enhancements seem only marginal. For example, the sign-change property, supported by Proposition A.8, Theorem 3.1, and Corollary 3.4, does not appear to be a significant contribution. Proposition A.8(a) is straightforward, and part (b) follows directly from result (23) in Proposition A.6, which is already known. Therefore, Proposition A.8(b) appears to be a simple consequence and could be considered "folklore" in the context of Wishart matrices.

2- **Difficulty to extend to other sparse RP settings**: The arguments presented here, based on rotation symmetries of the multivariate Gaussian distributions, seem difficult to adapt to the more practically relevant case of spare RP. In my view, it would be beneficial to discuss the potential challenges and limitations of extending their approach to sparse random projections, or discussing avenues for future work in the conclusion.


### Questions
1. The notation $ X_{u*}$ for the rows of a matrix is not explained prior to its use on line 115. It would help to define this notation when it first appears.

2.  On line 108, the authors suggest that computing $p(A)R^\top $ is faster than $p(A)$ alone. Could the authors clarify why this is the case?

3. It may improve clarity to introduce the power law either before or immediately following line 155.

4.  In line 281, the authors state that the interval endpoints are independent of the node degrees. Is this statement exact, or is it an approximation? Additional clarification would be beneficial here.

5. Proposition 2.6 seems straightforward. Is it necessary to present it formally as a proposition?

6.  For the ranking application, a more detailed explanation of the overarching goal would be helpful. Also, citations for the Normalized Discounted Cumulative Gain (NDCG) metric would add valuable context.

7. The definition of  $\text{rank}^R_w(h)$ is missing, and notation in this section could be streamlined to be consistent with the rest of the paper. For example, $NDCG(r^K_i, \hat{r}^K_i)$ is not defined.

8. There are some citation formatting issues in the appendix, such as on line 1079, where several references are improperly displayed.

9. It would be helpful to more clearly indicate which results in the appendix are novel contributions.

10. You establish a comparision with the results about cosine similarity of (Arpit et al. 2014) in section A.IV.5, but this not mentioned in the related work section. Indeed, the related work section, it could be mentioned which of the cited articles, and how, can be compared with the results here. For instance, you compare in Section A.III.5 the concentration results for $\frac{\langle Rx,Ry\rangle}{\|x\|\|y\|}$ with the  resullts in (Vempala, 2004) and (Kaban, 2015).

11-Could you please address the point I raised in the weaknesses section?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper examines the problem of embedding an adjacency/transition matrix using random projection through the lens of preserving dot product and cosine similarity. The paper provide both asymptotic and finite sample results that compares the two, and furthermore investigates this problem in a ranking configuration.

### Strengths
1. The paper provides an interesting analysis supported by theorems alongside their interpretations that make the results more clear. 
2. The ranking application is interesting, and is supported by proofs as well.

### Weaknesses
See questions.

A. As the authors wrote, random projection has guarantees with respect to the Euclidean distance preservation (Based on the JL lemma). I wonder how well would the regular random projection perform (in terms of dot product preservation) if the rows of the adjacency/translation matrix would have been normalized (using the L2 norm) before the projection. If space permits, I would suggest the authors to add a brief discussion or even analysis of this case. This could provide valuable context on the robustness of the findings
and a more comprehensive comparison of approaches. Specifically, it would be beneficial to understand the trade-offs between preserving the dot product when applying L2 normalization before projection versus the proposed method of using cosine similarity, which implicitly normalizes after projection. A quantitative comparison, perhaps through a small-scale experiment or theoretical analysis, would strengthen the justification for the chosen approach.

B. The assumption that the adjacency matrix is composed of only integers numbers should appear at the beginning of section 2. Currently it first appears in the proof of Lemma 2.1 in line 138. I recommend to add a clear statement about the integer assumption for the adjacency matrix in the opening paragraph or definitions of Section 2. Also, I would suggest to note or even briefly discuss the implications of this assumption, given that adjacency matrices in some applications may be continuous. For instance, how would the theoretical results change if the entries were drawn from a continuous distribution? Would the error bounds still hold, or would they need to be adjusted? Addressing these questions would broaden the applicability of the paper's findings.

C. The definition of  rank_w^R(h) that was used in line 315 is missing. I suggest to add a brief definition of it where it is first introduced, perhaps with a simple example to illustrate its meaning in the context of the ranking application. For example, if we have a set of items ranked by two different methods, how would rank_w^R(h) quantify the agreement between these rankings, considering the weights assigned to each item? A clear definition and illustrative example would significantly improve the readability and understanding of the ranking analysis.

### Questions
A. As the authors wrote, random projection has guarantees with respect to the Euclidean distance preservation (Based on the JL lemma). I wonder how well would the regular random projection perform (in terms of dot product preservation) if the rows of the adjacency/translation matrix would have been normalized (using the L2 norm) before the projection. If space permits, I would suggest the authors to add a brief discussion or even analysis of this case. This could provide valuable context on the robustness of the findings 
and a more comprehensive comparison of approaches.


B. The assumption that the adjacency matrix is composed of only integers numbers should appear at the beginning of section 2. Currently it first appears in the proof of Lemma 2.1 in line 138. I recommend to add a clear statement about the integer assumption for the adjacency matrix in the opening paragraph or definitions of Section 2. Also, I would suggest to note or even briefly discuss the implications of this assumption, given that adjacency matrices in some applications may be continuous.


C. The definition of  rank_w^R(h) that was used in line 315 is missing. I suggest to add a brief definition of it where it is first introduced, perhaps with a simple example to illustrate its meaning in the context of the ranking application.


Insights: The adjacency matrix configuration that you analyzed can be applied to problems in Natural Language Processing.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors investigate low dimensional embeddings of graphs via random projections, and in particular investigate dot product/cosine similarity preservation under such a setting, and apply it to a ranking application. The main contributions of this paper are theoretically motivated, as the authors attempt to show that under a natural definition of relevance, the cosine similarity will have better approximation properties under random projections than the dot product, and better stability in the case of ranking.

### Strengths
originality: the paper produces some original results theoretically on the analysis of dot product vs cosine similarity in the random projection setting for graphs. This line of investigation is original, to the best of my knowledge. 
quality:  I discuss the quality of this paper in the next section. Overall, I believe the mathematical derivations concluded in this paper are sound, but the quality of the exposition, motivation, and logical flow has much room for improvement. 
clarity: Overall, clarity is not a strength of this paper. However, The first two pages introducing the paper and the contributions are written clearly. 
significance: The broader topic of analyzing graph embeddings is certainly a significant direction of investigation. The application of ranking is also a significant avenue.

### Weaknesses
I raise questions and remarks along several front： 

1. Motivation: The the elephant in the room when considering the paper's line of investigation in terms of motivation and significance is this: is if higher order connectivity of graphs is a main motivation, what is the advantage of considering random projections versus spectral embedding approaches (It is clear that the eigendecomposition based approaches capture connectivity and matrix powers very well from spectral graph theory). I understand that this is a theory paper and I do not expect experiments comparing the two, but some sort of high level explanation/discussion seems warranted to convince the reader that it is worth the effort to develop theory for random projections. Specifically, a discussion on the computational complexity of random projections versus spectral methods for large graphs, especially in the context of dynamic or evolving graphs, would be beneficial. Furthermore, while the Johnson-Lindenstrauss lemma is mentioned in the context of large graphs, the theoretical results in Theorem 2.2a seem to diverge from this by considering an asymptotic regime with a root q scaling. Clarifying the practical implications of this scaling, especially in the context of large n, and how it relates to the log n scaling typically associated with random projections would greatly improve the motivation.

Minor point: -  the introduction of the NDCG metric was without citation/reference/background motivation in page 6. I suggest adding motivation. 

2. The mathematical results are not presented in a very organized/clear way. 

In the statement of the theorems, e.g. theorem 2.2, there is little indication of what setting the theorem corresponds to. In theorem 2.2a, the term "large q" is used in this asymptotic result, presumably indicating q is being sent to infinity, but the term q also appears on the variance term on the right hand side...one has to look at the remark below to see that this is explained by the somewhat nonstandard notation \sim_a to indicate a root q scaling. Results like these could be stated a lot more clearly. For example, explicitly defining the scaling relationship between q and n in the theorem statement would help. Additionally, providing a clear definition of the notation \sim_a at the beginning of Section 2 would prevent confusion. I highly suggest the authors expand the statements in the theorem to state exactly the definitions/constructions used in the setting and the regularity/structural assumptions that they are referring to for clarity. 

I say this NOT to indicate that the mathematical derivation is wrong (even though I did not check proofs in appendix line by line, the mathematical results here overall look ok to me), but to indicate that the lack of clarity in the write up and the statements of the theorems make it very difficult for readers to properly check the math and keep track of the exact setting/assumptions that the particular theorems are referring to. Connecting the theoretical results, to the recommendations in the discussion section, becomes even harder given the somewhat disorganized nature of the presentation. 

3. The organization of the paper can be improved: 
- the subsection titles are not well organized. Section 2.1 is RP DOT PRODUCT WHEN P = T, and seeing this one naturally expects 2.2 to be P = A, but turns out that is delegated to the appendix, and 2.2 goes to cosine similarity where P = A and T are both considered since they don't make a difference. I suggest making 2.1 heading just RP dot product, and then consider the subcases P = T etc within the section rather than on the title. Ditto for the stability subsection titles in section 3. 

Given the above, my belief is that the paper can be substantially improved in the presentation, clarity and organization front.

### Questions
See comments above.

### Soundness
2

### Presentation
1

### Contribution
2

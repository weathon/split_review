# Not All Language Model Features Are Linear

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Recent work has proposed that language models perform computation by manipulating one-dimensional representations of concepts (``features'') in activation space. In contrast, we explore whether some language model representations may be inherently multi-dimensional. We begin by developing a rigorous definition of irreducible multi-dimensional features based on whether they can be decomposed into either independent or non-co-occurring lower-dimensional features. Motivated by these definitions, we design a scalable method that uses sparse autoencoders to automatically find multi-dimensional features in GPT-2 and Mistral 7B. These auto-discovered features include strikingly interpretable examples, e.g. \textit{circular} features representing days of the week and months of the year. We identify tasks where these exact circles are used to solve computational problems involving modular arithmetic in days of the week and months of the year. Next, we provide evidence that these circular features are indeed the fundamental unit of computation in these tasks with intervention experiments on Mistral 7B and Llama 3 8B. Finally, we find further circular representations by breaking down the hidden states for these tasks into interpretable components, and we examine the continuity of the days of the week feature in Mistral 7B.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper calls into question the Linear Representation Hypothesis (LRH), in particular the part that claims the representations of features in LLMs lie along one-dimensional lines. 
A clear visual example is provided in Figure 1, where a circular feature for days of the week is shown in a 2-dimensional PCA space.
The paper then formally defines irreducible, multi-dimensional features and proposes an updated version of Elhage et al.'s Linear Superposition Hypothesis to incorporate multi-dimensional features.
The specific definition of irreducibility is further used to derive a clustering-based method to automatically find irreducible features among the dictionary elements learned by sparse autoencoders (SAEs) trained on LLMs.
Finally, the paper illustrates how steering the circular feature of day-of-week can alter the model's output in synthetic tasks.

### Strengths
- The paper tackles a timely and important question in mechanistic interpretability by formalizing (inherently) multi-dimensional features in LLMs.
- The visual examples of circular representations are clear and compelling.
- I think the high-level idea of formalizing multi-dimensional, irreducible features is sensible and useful.
- Overall, the experiments are comprehensive with a variety of interesting results.

### Weaknesses
 - I think there are some conceptual questions about the definitions of features and irreducibility.
    - Conceptually, I think the definition of irreducibility is somewhat incomplete. First, there can be concepts that are correlated but can still be disentangled for separate interventions, so equating separability with independence is can be limiting. Second, I can't tell for sure if the definition of reducibility is exhaustive. (Can there be a third category?)
    - I have asked about some of the more specific unclear points in the questions below.
- While the paper's main motivation is to call the LRH into question, the proposed alternative hypothesis appears to be a stricter version of the LRH (p. 5, lines 239--240), rather than a contradiction to it. This makes the overall message a bit confusing. (I'd be happy to be corrected if this is a misunderstanding.)
- The proposed "tests" of irreducibility are not completely formal, in the sense that they are not statistical tests of significance but rather (possibly arbitrary) thresholding of a pair of metrics. This could mean that whether or not a feature is irreducible is ultimately a judgment call by the user.
    - To be clear, I'm not saying this is something that can be readily addressed; it's a limitation that should be mentioned somewhere.
- For the intervention tests, I'm not fully sure if the results demonstrate "causal implication" of the circular feature. The results are interesting, but I'm not sure if they are conclusive. See second-to-last question below.
- Despite its interesting results, the paper's exposition is not very clear.
    - I find that Section 3 is not easy to follow. The only visual aid is Figure 2, but it is not referenced or intuitive.
        - E.g., why exactly are we looking at PCA 2/3, even for Fig. 1? What is the histogram in the middle, and what is the angle on the right? What are "typical clusters" and what are their mixture/separability indices?
        - I believe some of these are answered in the referenced Appendix. While I am okay with most computational details being deferred to the Appendix, at least the plots should be self-contained. Also, some of the key computational details should be noted (that separability index is computed in 2-d and that mixture index is computed approximately via SGD). Otherwise, the exposition is quite hard to follow.
    - While some of the plots are great, the experiments are quite dense and unorganized. The exposition would often refer to a figure in the Appendix, while some figures (2 and 4) in the main text are not referenced. This makes it difficult to read the paper linearly.
        - I would recommend starting each subsection with a clear motivation, the key result(s), and then reference supplementary results in the Appendix.
        - Perhaps a few more plots can be moved to the Appendix in favor of more explanation/motivation/examples.

### Questions
- Figure 1: is there any intuition for why specifically we find these features in the second and third PCA components? 
- Definition 1: What exactly is a $d_f$-dimensional point cloud in $\mathbb{R}^{d_f}$? Is there a mathematical definition? (Is $d_f$ redundant?) If I have two points in $\mathbb{R}^3$, what is the "dimension" of the point cloud they form?
- Also, to be precise, should I understand the "probability distribution over input tokens" as that of the natural language? I also assume that this probability is restricted to $n$-length token sequences---is that correct? 
  - Later, in the definition of the two indices, the distribution comes up anyway as $\mathbb{P}$. It may be helpful to formally define this notation/distribution up front.
- Definition 2: in the mixture definition, what is the non-bold $b$? Also, does "lower dimensional" simply mean $k < d_f/2$ or does it mean low-dimensional, say, $k \ll d_f$?
- Is there intuition as to why it suffices to consider separable and disjoint features as the two types of reducible features? Could there be other types of reducible features?
- Can you efficiently compute the separability index for features that are beyond two-dimensional?
- Hypothesis 2: while this is a stylistic point, I think the use of a possessive in "Our Superposition Hypothesis" is unnecessary and un-scientific. It could have any other objective name, say, the "Multi-Dimensional Superposition Hypothesis". See, e.g., [Knuth et al.](https://jmlr.csail.mit.edu/reviewing-papers/knuth_mathematical_writing.pdf), page 2 item 6.
- p. 5, lines 260--270: doesn't this claim depend heavily on (1) the two-dimensional feature being active in the LLM's representation space and (2) the SAE is large enough to capture this feature? I'm not even sure if this claim is necessary, as opposed to saying "some of SAE clusters represent irreducible features".
- Figure 3: what are some of the other features that are shown  here to be more reducible than the features for Fig. 1?
- Are there any other features that we may intuitively view as circular but not found by the SAE? Say, are color words (red-orange-yellow-green-blue-purple) represented in a circular fashion?
- p. 8, "In practice, ...": this is somewhat confusing/concerning to me. If there are alternative pathways that may affect both the circular feature and the task output, then wouldn't they "wash away" the causal implication of the feature? In other words, in what sense exactly is this a "causal" implication rather than correlational?
- Broad question: are there examples of multi-dimensional features that aren't circular?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work's main focus is to set a theoretical framework for irreducible multidimensional features and to show their concrete existence in real-life LLMs. In particular, the authors: 
- update the superposition definition to account for irreducible multi-dimensional features.
- propose an algorithm that---using an SAE-learned dictionary---identifies possible multi-dimensional features. 
- show evidence of features expressing circular behavior for the representation (and manipulation) of periodic data, such as months, weeks, and days. The models whose features are shown to exist are non-toy models, such as Llama 3 8B and Mistral 7B, further increasing their argument's validity.

### Strengths
1) The updated proposed definition for the superposition hypothesis is sound and may lead to the discovery of other interesting structures such as the ones presented in the paper. Even if this direction does not lead to further scientific discoveries, the discovered representations themselves are an interesting finding.

2) In the paper, features are extracted from state-of-the-art LLMs, showcasing the existence of actual multi-dimensional features of circular nature **"in the wild"**.

### Weaknesses
1) If I understand correctly, the proposed algorithm can extract interpretable features, however, I imagine there is a good amount of them that is not easily--if at all--interpretable. Adding some of your insight on how many potentially interesting multi-dimensional features are among the ones extracted from the algorithm could improve the article. Specifically, it would be useful to know the proportion of extracted features that exhibit clear multi-dimensional structure versus those that appear to be noisy or unstructured. A more detailed analysis of the distribution of feature dimensionalities would also be beneficial.

2) If I am not mistaken, there is not an ablation on how much the threshold parameter T affects the extracted clusters: Having an understanding of when circular features start to emerge could be an interesting experiment to add, and may potentially lead to some useful insights. It would be helpful to see a more systematic exploration of how different values of T impact the clustering results, and whether there is a critical threshold at which the circular structures become apparent. Furthermore, it would be beneficial to understand how the choice of T affects the overall number of clusters and the size of each cluster.

3) Figures 2 and 3 can be improved in their overall presentation:
- Figure 2: I would change the color for the PCAs scatter plot from black to something with less contrast (e.g. the green used in the angle subfigure of  Figure 2)
- Figure 3:  This is a very minor complaint, but I would change the scatter icon for the "other cluster" points to something different than the one used to indicate the clusters shown in Figure 1, for example, something like an **x** would probably look a bit better.

4) Another minor issue is that the captions for Figures 5 and 6 are a bit lacking, adding some more information to help understand their respective feature would probably be helpful.

### Questions
1) Do you have any qualitative insights on how big the threshold parameter T should be in order to find multidimensional features?

2) Are there any extracted multi-dimensional features that show some interesting behavior, like the circular one shown in the paper? If not, do you think is it due to a structure difficult to interpret, or simply because probably most of the features are still one-dimensional?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors define multi-dimensional features and identify these representations empirically using sparse autoencoders. They also show that some LLMs use circular representations for days of the week and months of the year to perform modular addition.

### Strengths
The extension of the linear representation hypothesis from one-dimensional to multi-dimensional one provides good insights for researchers in the mechanistic interpretability field. Concrete and extensive empirical results show that multi-dimensional features exist in LLMs. In particular, the circular representations of days of the week are interesting.

### Weaknesses
Some details in formalization and experiments are not clear. Please see the questions below.

1. As you mentioned, the title is confusing. How about 'Not All Language Model Features are One-dimensionally Linear'?
2. Why do you use the term 'point cloud' in Definition 1? Does it mean that the range of the map $f$ is a discrete set?
3. What is the source of randomness for $p(a,b)$ in Definition 2? Does it come from the distribution of input texts (in training set for LLMs)? Also, why do you state that statistical independence and separability are equivalent?
4. In Figure 2, the histogram appears to show a mixture. Why did you say that the $\epsilon$-mixture index of 0.4750 is low? What is the baseline? In Figure 10, you state that an index of 0.3621 indicates the feature is likely a mixture. This seems contradictory.
5. In line 269, why do you state that 'These dictionary elements will then have a high cosine similarity'? I believe they could have low cosine similarity even if many elements span the feature.
6. In Figure 1, how were the points labeled? What does the label 'Monday' mean? Does it indicate that 'Monday' would be the next token in the corresponding texts?
7. In Section 5, you use specific texts and train new probes. Why didn't you use the circular representations previously identified by SAE clustering?

### Questions
1. As you mentioned, the title is confusing. How about 'Not All Language Model Features are One-dimensionally Linear'?
2. Why do you use the term 'point cloud' in Definition 1? Does it mean that the range of the map $f$ is a discrete set?
3. What is the source of randomness for $p(a,b)$ in Definition 2? Does it come from the distribution of input texts (in training set for LLMs)? Also, why do you state that statistical independence and separability are equivalent?
4. In Figure 2, the histogram appears to show a mixture. Why did you say that the $\epsilon$-mixture index of 0.4750 is low? What is the baseline? In Figure 10, you state that an index of 0.3621 indicates the feature is likely a mixture. This seems contradictory.
5. In line 269, why do you state that 'These dictionary elements will then have a high cosine similarity'? I believe they could have low cosine similarity even if many elements span the feature.
6. In Figure 1, how were the points labeled? What does the label 'Monday' mean? Does it indicate that 'Monday' would be the next token in the corresponding texts?
7. In Section 5, you use specific texts and train new probes. Why didn't you use the circular representations previously identified by SAE clustering?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors show convincingly that large language models have circular representations of periodic variables, and provide a means of discovering and probing these representations using sparse autoencoders and causal interventions.

### Strengths
The results are straightforward, and backed up by causal experiments. Clearly connects to existing methods in the interpretability field, which could make it simple for others to replicate.

### Weaknesses
The clustering method was a little hard to follow for me at first, maybe pseudocode would be helpful (since it seems like it wouldn't be many lines).

Is it mostly just circles? Given that they are still a one-dimensional variable, I'm wondering whether there are representations of variables with (irreducible) intrinsic dimension higher than one (like a spherical variable), which would seem to make better use of the scope of your Hypothesis 2. Otherwise, maybe the linear representation hypothesis has been violated in name but not in spirit (i.e. representation is still factorized into one-dimensional variables)?

### Questions
Is it mostly just circles? Given that they are still a one-dimensional variable, I'm wondering whether there are representations of variables with (irreducible) intrinsic dimension higher than one (like a spherical variable), which would seem to make better use of the scope of your Hypothesis 2. Otherwise, maybe the linear representation hypothesis has been violated in name but not in spirit (i.e. representation is still factorized into one-dimensional variables)?

### Soundness
3

### Presentation
3

### Contribution
3

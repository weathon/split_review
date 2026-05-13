# softmax is not enough (for sharp out-of-distribution)

- Decision: Reject
- Scores: 6, 8, 5, 6, 6

## Abstract
A key property of reasoning systems is the ability to make \emph{sharp} decisions on their input data. For contemporary AI systems, a key carrier of sharp behaviour is the \texttt{softmax} function, with its capability to perform differentiable query-key lookups. It is a common belief that the predictive power of networks leveraging \texttt{softmax} arises from ``circuits'' which sharply perform certain kinds of computations consistently across many diverse inputs. However, for these circuits to be robust, they would need to generalise well to \emph{arbitrary} valid inputs. In this paper, we dispel this myth: even for tasks as simple as finding the maximum key, any learned circuitry \emph{must disperse} as the number of items grows at test time. We attribute this to a fundamental limitation of the \texttt{softmax} function to robustly approximate sharp functions, prove this phenomenon theoretically, and propose \emph{adaptive temperature} as an ad-hoc technique for improving the sharpness of \texttt{softmax} at inference time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper explores the fundamental limit of the Softmax activation function, which is frequently used to model attentional mechanisms of machine learning, for OODs generalization in reasoning tasks that require sharpness (e.g. finding maxima or second maxima) by exploring a simple _max retrieval_ task. The paper claims that even in that simple task, the networks using Softmax cannot generalize well (length generalization) in those tasks, because it cannot approximate the sharpness with increasing problem size (dispersed property). The paper backs its claim with both theoretical analysis and empirical experiments. Moreover, the paper also proposes a simple method to (somehow) alleviate this dispersed property by proposing an adaptive temperature scaling method.

### Strengths
The paper is well-written and easy to follow. The setting and motivation are clear, though it is a bit niche (focus on OODs generalization for tasks that strictly require sharpness). The findings are interesting (though the formal claims have some potential issues, see Weaknesses), and the proposed method is promising.

### Weaknesses
First things first, I admit that I am not an expert in this topic. I will leave comments on the novelty and soundness of this paper to other reviewers. Here are some other comments:

## Comments on mathematical notions
There are some potential typos in mathematical notions in this paper, for example:

1. The definition of _sharp function_ in Line 50 is not clear to me. Concretely, I do not think that the $\max$ function only depends on the constant number of its inputs, since it must examine all the inputs to output the maximum number. I think the better statement would be "the $\max$ function output value equal to the value of one of the inputs". But it would definitely break the _sharp function_ definition above.

2. The statement of Theorem 2 and its proof is not rigorous. Here in the statement, the authors say that "$\mathcal{X} \in \mathbb{R}^m$ be an $m$-dimensional input feature _space_", but later say that $|\mathcal{X}| < \infty$. This mathematically means that $\mathcal{X} = \\{\mathbf{0} \\}$, where $\mathbf{0} \in \mathbb{R}^m$. Maybe the authors mean something different (like _set_ instead of _space_?), but they should explicitly state it.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors show that the ubiquitous softmax function must provably disperse (i.e. converge to the uniform distribution) as input length increases, so long as the inputs are bounded and the temperature is non-zero. As a result, any softmax-based model where such conditions hold true (e.g. a transformer with a finite vocabulary) cannot approximate sharpness with increasing input lengths. These models therefore cannot generalize out-of-distribution to longer problems, and will fail on tasks where learning sharpness or a low-entropy distribution matter.

In the second part of the paper, the authors propose a fix for the softmax, where the softmax temperature $\theta$ is allowed to vary as a function of input entropy. They (a) demonstrate their approach on a toy problem of max retrieval as well as (b) evaluate it on the CLRS-Text benchmark suite using finetuned Gemma 2B models.

### Strengths
1. The paper is, overall, well-written and pleasant to read. The text is lucid and careful, and the diagrams are illustrative. In general, I was able to follow along easily without any confusion.

2. Section 2 is well-constructed and compelling. Even though the conclusions of Lemma 2.1 and Theorem 2.2 are relatively simple and follow directly from compactness of the input features, this work is (to the best of my knowledge) the first to emphasize the link between softmax and sharpness approximation, and consequently, the negative impact on a transformer's ability to generalize to longer problems. These theoretical findings are also backed up by empirical results on a toy dataset. Overall, this is an important observation that is worth highlighting.

3. The authors try to provide a fix in the form of an adaptive temperature parameter, and demonstrate some results on both toy and real-world datasets.

### Weaknesses
1. It is a little unclear how significant of a problem the dispersive issue with softmax actually is. As the authors themselves have noted, in various prior work studying transformer mechanisms, the heads appear to be sharp. Whether softmax is "sufficiently" sharp is, after all, dataset and problem dependent. Without a more comprehensive evaluation on real-world datasets, it is hard to tell if the problem is overstated. 

2. In general, I think the latter half (Sections 3 and 4) is less compelling:

    - It is not clear from the empirical results that merely having an adaptive temperature parameter is a meaningful fix to counter the dispersive tendencies of softmax. E.g. the results in Table 1 are mostly incremental and the visual differences in Figure 6 are minor. 

    - As noted by the authors themselves, the correct adaptive function for $\theta$ is dataset-dependent and determining what this function is can be highly non-trivial in attention models. 

    - Related to my first point above, but I think evaluation is a little limited in terms of real-world datasets. It is not entirely clear that adaptive temperature softmax makes a significant difference on a real-world natural-language dataset, e.g. I am curious if it would actually improve on a, say, Q&A task where we want to generalize to answers of different lengths.

### Questions
1.  The details of Section 4.2 are a little vague to me. This paragraph: 

```
That being said, there is an alternate route to make the Gemma model still benefit from our adaptive
temperature module exactly as-is; it just has to directly learn how to leverage it. As such, in our
CLRS-Text ablation we apply adaptive temperature both during fine-tuning and at inference time.
```

is not entirely clear to me, would the authors be able to explain how exactly adaptive
temperature is implemented here?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the limitations of the softmax function in modern AI. Although softmax is widely used for sharp decision-making in AI, the authors highlight how softmax suffers from dispersion as input data grows. This limits its effectiveness in out-of-distribution scenarios. The authors theoretically establish that softmax inevitably disperses as input grows, preventing sharp focus on specific items in larger datasets. To address dispersion, the authors propose an adaptive temperature mechanism that adjusts softmax sharpness by tuning temperature based on entropy. The authors demonstrate the effectiveness of the proposed method in experiments.

### Strengths
* The paper provides a theoretical perspective on the limitations of the softmax function, specifically its inability to maintain sharpness across increasing input sizes.
* The introduction of adaptive temperature as a method to mitigate softmax dispersion is well-motivated.

### Weaknesses
* Out of distribution is a key word in this work but the authors do not provide clear definition under the context.
* The performance of proposed method on real-world tasks or datasets is not extensively covered. Additionally, results on only a few benchmarks limit the generalizability of conclusions.
* Although adaptive temperature is a good idea, its implementation could introduce computational tuning complexity, especially in models with many attention heads or large-scale data. 
* Not include experiments that assess the scalability of adaptive temperature, especially for high-dimensional, high-volume data.

### Questions
In page 1: "Here we call a function sharp if its output only depends on a constant number of its inputs (e.g.max)."
Why does max function only depends on a constant number of its inputs? It is not quit clear here.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper aims to show that the widely-used softmax layer must inevitably disperse the output prediction on the out-of-distribution data set. To address this issue, the authors propose an adaptive-temperature technique to improve the sharpness.

### Strengths
Overall, I think the paper discusses a quite interesting topic that softmax will basically eventually fail on the out-of-distribution test. The conclusion is indeed supported by some theoretical results and numerical experiments. A partial solution based on adaptive temperature is also provided.

### Weaknesses
The theoretical results are not very solid. The presentation needs improvement due to some unclear statements. Adaptive temperature seems only slightly improves the performance.

### Questions
- The word ``disperse" appears at the very beginning of the paper. It deserves a precise mathematical definition. I think it should mean that the output distribution will eventually converge to a uniform distribution.

- In Lemma 2.1, the notation $\Theta(\frac{1}{n})$ is used. What is that? I guess it should mean "in the order of $\frac{1}{n}$" according to (4). In fact, the exponential function in (4) quite alerts me. For large $\delta$, these bounds should vary a lot, not behaving like $\Theta(\frac{1}{n})$.

- When considering deep learning's performance on out-of-distribution data, I think it is not surprise at all to see the failure of softmax due to the new statistic information. A more interesting question should be how to quantify it, i.e., the how much change in the output of softmax responds to the change in the distribution of input data.

- Theorem 2.2 seems only consider the worst scenario as it works for networks with any parameters. But this is certainly not true in practice, as those parameters are all trained to minimize the loss functions.
  
- It seems that Proposition 3.1 can be numerically verified.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors show that at inference time, the post-softmax of the self-attention layer will disperse as the input sequence length grows to infinity. This is due to the fact that softmax cannot approximate "sharpness" when the input is bounded. To address this limitation, the authors propose an inference-time procedure termed adaptive temperature, and conduct experiments on max retrieval and CLRS Text to validate its effectiveness.

### Strengths
- The topic of study is interesting 
- The discussion in Section 5 could potentially inspire future research

### Weaknesses
There are at least two main weaknesses:

- The presentation is unsatisfactory in several ways: 1) There is no preliminary section introducing the basics of transformers (and others), and all notations are squeezed into the statement of Theorem 1; 2) Many unconventional terms, such as "attentional head" and "attention coefficients", are used frequently without definitions or explanations; 3) The figure captions are overly brief and impede understanding, for example, it is unclear what "batch" refers to or what each row represents in Figure 2, the meaning of the different curves and the shaded blue region in Figure 3 is not explained, and the x-axis in Figure 7 is unclear, with the legend appearing only in one small figure (which could easily be overlooked); 4) The procedure for applying adaptive temperature is not formally described, which is necessary given that multiple self-attention modules are present across different layers in language models.

- The paper covers theory, algorithms, and experiments, but none of these components seem to be particularly strong, making it difficult to identify the main contribution of the paper.
  - **Theory**. The main result, Theorem 2, seems to be a straightforward corollary of Lemma 1 (relying on the fact that the continuous mapping of a compact set remains compact), which itself leverages a basic property of softmax. While I’m not advocating for fancy proof techniques, the real concern is that the conclusion of Theorem 2 feels unsatisfying. Specifically, 1) it is unclear what the consequence of such "dispersion" of attention coefficients is: does it imply the failure of the underlying reasoning task? Will it still be problematic if the ground truth token has a coefficient of $O(\frac{\log n}{n})$ while the other tokens have coefficients of $O(\frac{1}{n})$, where their *ratio* still goes to infinity? 2) The statement is too broad and applies equally to any self-attention module in a language model; a more interesting question might be whether self-attention modules in deeper (i.e., later) layers suffer more from this dispersion phenomenon.
  - **Algorithm**. The authors themselves acknowledge that adaptive temperature does not fundamentally address the dispersion issue, which is reflected in the experimental results. For example, in Table 1, the improvement over the simple baseline is not very significant.
  - **Experiments**. The paper mainly focuses on the max retrieval task. For the CLRS-Text benchmark, the authors adjusted their algorithm by applying adaptive temperature both at inference time and during fine-tuning. However, it’s unclear where the performance gains come from. Is approximating sharpness still relevant for these tasks? More broadly, what is the implication of the paper's results for general reasoning tasks?

While I appreciate the idea and topic of the study, the paper needs to address the presentation issues and strengthen **one** of the three aspects to be considered for acceptance. Note I think it is perfectly fine that a paper does not have significant algorithmic contributions. 

**Minor**: Although I’m not super familiar with the related work, two lines of research, length generalization and attention sink, could be relevant.

------------
**Post-rebuttal**: Acknowledging the authors' response and the revisions to the paper, I am increasing my score to 6. That said, I feel it is important to note that the changes made are substantial and should be taken into account when AC/SAC make their final decision.

### Questions
See above.

### Soundness
3

### Presentation
1

### Contribution
2

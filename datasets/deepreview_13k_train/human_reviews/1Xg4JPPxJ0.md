# Are Transformers Able to Reason by Connecting Separated Knowledge in Training Data?

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Humans exhibit remarkable compositional reasoning by integrating knowledge from various sources. For example, if someone learns ( B = f(A) ) from one source and ( C = g(B) ) from another, they can deduce the value of ( C ) by reasoning ( C=g(B)=g(f(A)) ) even without encountering ( ABC ) together, showcasing the generalization ability of human intelligence.  In this paper, we introduce a synthetic learning task, ``FTCT" (Fragmented at Training, Chained at Testing), to validate the potential of  Transformers in replicating this skill and interpret its inner mechanism. In the training phase, data consist of separated knowledge fragments from an overall causal graph. During testing, Transformers must infer complete causal graph traces by integrating these fragments. Our findings demonstrate that few-shot Chain-of-Thought prompting enables Transformers to perform compositional reasoning on FTCT by revealing correct combinations of fragments, even if such combinations were absent in the training data. Furthermore, the emergence of compositional reasoning ability is strongly correlated with the model complexity and training-testing data similarity. We propose, both theoretically and empirically, that Transformers learn an underlying generalizable program from training, enabling effective compositional reasoning during testing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work sets out to investigate whether transformers are capable of generalizing to longer reasoning chains through connecting shorter ones seen in the training stage. The authors introduce "Fragemented at Training, Chained at Testing" learning task to train a randomly initialized 3-layer 3-head GPT2-like transformer. They find that with few-shot chain-of-thought prompting, transformers can perform good compositional reasoning skills by combineing fragments together. The authors further show that the generalization performance highly correlates to model complexity (require multiple-layer attention structure) and high relative knowledge ratio of training data. The paper also discusses the internal working of the model (learn an underlying generalizable program) to interpret the transformer's generalization behaviors and provide theoretical insights on transformer's expressivity on learning a such program.

### Strengths
1. The paper investigates whether transformers are capable of generalizing to longer reasoning chains through connecting shorter ones seen in the training stage, which is an interesting and important research question.
2. The paper is technically sound: the trained transformers behave compositionally (with few-shot chain-of-thought prompting) and the authors provide insights on its internal workings: induction head and attention assignment, demonstrating that the transformer learn a generalizable program in its internal computing.
3. Authors also theoretically prove that Transformers have the expressivity to simulate the generalizble underlying program.

### Weaknesses
1. Since the experiment setting is a randomly initialized transformer trained on synthetic data, to what extent the paper's conclusion can be extended to real pre-trained language models is questionable.
2. the notations used in the paper are quite complicated, making the paper a little bit difficult for readers to follow.

### Questions
1. In the FTCT learning task (e.g., Figure 1), why in the $D_{train}$, we need to add noisy tokens in the token sequence? Why in the $D_{test}$ we do not add noisy tokens in the prompt?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the "FTCT" (Fragmented at Training, Chained at Testing) task to evaluate if Transformers can perform compositional reasoning similar to humans. The task involves training models on separate knowledge fragments and testing them on integrating these fragments to form complete causal graph traces. The study finds that few-shot Chain-of-Thought prompting helps Transformers combine these fragments correctly, even without seeing such combinations during training. The results indicate that model complexity and the data's knowledge ratio play a role in enabling this skill. The authors provide theoretical and empirical evidence for their claims, showing that Transformers can learn a generalizable program to aid in compositional reasoning. The findings are interesting and suggest potential areas for further exploration.

### Strengths
- The design of the FTCT task is well-conceived, as it effectively mimics real-world scenarios where knowledge is often fragmented and must be integrated to draw comprehensive conclusions. This setup provides a meaningful and practical benchmark to evaluate the compositional reasoning abilities of Transformers, making the study relevant and valuable for advancing our understanding of machine learning models' capabilities.
- Chapter 5, "transformer does compositional reasoning via the underlying program", is very interesting as it explores the possible underlying mechanisms and principles that allow Transformers to perform compositional generalization. This chapter goes beyond just presenting empirical results by looking into how these models might internally handle and integrate fragmented knowledge. This deeper investigation adds value by giving us a better understanding of how Transformers achieve complex reasoning tasks.

### Weaknesses
 - While the task studied in this paper requires strong compositional generalization abilities, it is simple and singular in its form. Generally, using a simple and singular synthetic dataset is suitable for highlighting the shortcomings of the Transformer architecture. However, since the paper concludes that Transformers possess this capability, the experiments on this task alone are not sufficient to support such a conclusion. I believe that more diverse and comprehensive tasks are needed, and ideally, this capability should also be validated on complex real-world tasks. Specifically, the FTCT task, while well-defined, lacks the complexity found in real-world scenarios where causal relationships are often intertwined with various contextual factors and require more nuanced reasoning. The current task focuses on a very specific type of causal chain, which may not generalize to more complex causal structures involving multiple interacting variables or feedback loops.
- In the related work section, the paper discusses various tasks used to probe compositional generalization abilities. The authors mention that these existing tasks have not been studied from the perspectives of few-shot prompting and chain-of-thought reasoning. However, this distinction alone is insufficient; if the difference is merely in this aspect, it would be possible to modify existing datasets instead of creating a new one. The novelty of this newly created task is not demonstrated well. Therefore, the authors need to provide more explanation regarding the motivation and innovation behind the proposed task. The paper does not adequately explain why existing compositional generalization benchmarks cannot be adapted to include few-shot prompting and chain-of-thought reasoning. A more thorough justification is needed to highlight the unique contribution of the FTCT task beyond simply adding these prompting techniques.
- The experiments in this paper use Transformers with relatively small parameter sizes. It is unclear whether the conclusions drawn from these experiments would hold true for larger Transformer models. This limitation raises questions about the generalizability of the findings to more complex and sizable architectures. The paper should include experiments with larger models to demonstrate that the observed compositional reasoning abilities are not simply an artifact of the specific model size used. Without this, the claims about the general capabilities of Transformers in compositional reasoning remain unconvincing.

### Questions
My main concerns have already been expressed in the "weakness" section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates how well transformers are able to perform compositional reasoning tasks. To that end, the paper introduces a new dataset methodology, namely the Fragmented Training, Chained at Testing (FTCT) that simulates how models would be presented with training data in practice (with incomplete fragments of reasoning paths with noise + context) and how well the model is able to piece together the full reasoning chain in test-time. Using this methodology, the paper runs insightful experiments that ablate different lengths of partial reasoning chains during training, different transformers and neural architectures, and number of few shot CoT examples. Through these experiments, the authors find that few shot CoT plays an important role for compositional reasoning, the impact of increasing relative knowledge ratio, and the increasing expressibility of adding layers and heads in the transformers architecture. Lastly, the paper presented some empirical evidence that you need a certain complexity of the transformers architecture to simulate the optimal program for the FTCT task in training and testing.

### Strengths
- The paper presented a very intriguing and creative approach to testing the ability for models to learn compositional reasoning ability
- There are some really interesting results, specifically the exact complexity (and the increased expressability) needed for the transformer architecture to optimally solve the FTCT task
- The insights regarding the few shot CoT results are of significance and spark further research in this area
- The empirical findings of how the transformers performs this task is enlightening and should spark some interest for further research in this area

### Weaknesses
 - The clarity of this paper is lacking, especially in the notation and writing. For instance, in Figure 1, there is a seeming typo in some of the values that contradicts the setup of the dataset. Separately, some concrete examples of the data (including noise + context tokens) of the FTCT dataset would really improve the readers understanding (it took me multiple re-read to get the gist of the methodology). Specifically, the description of how the noise tokens are incorporated and their values are assigned is not clear. The notation used in Section 3, particularly in the description of the 'Downstream Processing' step, is overly abstract and makes it difficult to understand the exact input format to the model. For example, the use of  $o^{\texttt{cm}}$ and $o^{\texttt{eq}}$ without clear definitions makes the processing steps opaque. Furthermore, the description of how the model processes the input sequence with context and noise is not clear, and concrete examples would be beneficial.
- The paper's definition of compositional reasoning should be explicitly written out in the paper. The only real definition of this is in the abstract where it is stated that "For example, if someone learns ( B = f(A) ) from one source and ( C = g(B) ) from another, they can deduce ( C = g(f(A)) ) effortlessly, even without encountering ( AC ) or ( ABC ) together, showcasing their compositional generalization ability."
- With this FTCT methodology, it seems clear that the model is learning some ability to connect sequential reasoning chains together (e.g. during training the model might just as AB and BC and correctly chain ABC), but the approach does not test if the model can correctly reason about AC in test-time, which is an aspect of compositional reasoning (as mentioned in the abstract). It is unclear if the model is truly performing compositional reasoning or simply learning to chain adjacent vertices together. The methodology does not explicitly evaluate the model's ability to perform reasoning across non-adjacent vertices, which is a key aspect of compositional generalization.

### Questions
- Although it is clear that the model is learning some ability to connect reasoning chains together (e.g. during training the model might just as AB and BC and correctly chain ABC), will the model be able to correctly chain together the values of AC? This could make for an interesting experiment where we could have some skip links in the test data and check for values accuracy
- Checking my understanding, is there a typo in Figure 1, where B=106 and B=103, should it be C=108 and C=105, respectively?
- Are there more than one set of the causal chains? The set equation in line 155 seems to suggest there is only one sequence of length n.
- Why are the noise vertices inserted in a predictable manner?
- I am curious about this 0.3 relative knowledge ratio threshold where it is reported that compositional reasoning emerges. Could it be that 0.3 is when the probability that there is at-least one occurrence for every (v_i, v_{i+1}) in the train set reaches close to 1? 
- Why is there a drop in performance in Figure 2 (right) and relative knowledge of 0.25?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
**Aims:** This paper seeks to understand at a mechanistic level how Transformers are able to perform compositional reasoning in a few-shot chain-of-thought setting.

**Methods:** A synthetic dataset is generated consisting of chains of nodes and edges derived from causal graphs. At training time, spurious nodes are inserted randomly into the chains; at testing time, few-shot prompts consisting of intact chains (no spurious nodes) are provided to the model. Models are tested on their ability to reconstruct full causal chains from fragmented chains learned in training, with evaluation based on accuracy in predicting both the correct vertex order and values in the chain.

**Results:**

- Zero-shot versus few-shot prompting is compared, with findings showing that few-shot CoT prompting significantly enhances performance in compositional reasoning tasks, particularly in forming the correct vertex order.
- A space of small, GPT-2-style models ranging from 42M-54M parameters are trained on the FTCT dataset. Results show that multi-layer, multi-head Transformers (minimum 2 layers and 2 heads) perform notably better, while single-layer/single-head models and MLPs perform poorly.
- The impact of training data’s relative knowledge ratio (ratio of child chain length to complete chain length) is studied, with a critical threshold (ratio ≥ 0.3) identified where compositional reasoning reliably emerges.
- Mechanisms underlying the model's success, such as induction heads for in-context learning and attention patterns facilitating parent-child relationships, are analyzed through linear probing, revealing specific mechanisms by which the model achieves compositional reasoning.

### Strengths
**Motivation:** The key research questions of the paper are clearly delineated in the introduction:

1) When are Transformers able to perform compositional reasoning by connecting fragmented knowledge in training data?
2) How do different training factors impact the emergence of this ability?
3) What internal mechanisms enable Transformers to develop this ability?

These questions are broadly relevant to current research and the paper is structured in a way that consistently centers these 3 questions throughout.

**Mechanistic interpretability analysis:** I especially enjoyed the approach to question (3). Broadly speaking, the authors approach this question by first demonstrating that there exists a program that solves the task (Sec. 5.1) and that this program can be approximated by a 2-layer Transformer (Sec. 5.2). Then, through linear probing experiments (Sec. 6), they give an empirical argument that the Transformers trained on FTCT have learn to implement this program. I am not an expert on probing so I can’t speak to the soundness of the methods, but I found the combination of Sec. 5-6 to be an elegant argument from a mechanistic interpretability standpoint.

### Weaknesses
 **Novelty:** The paper claims to “introduce a learning task” (FTCT) based on causal graphs, and yet the design of this task is nearly identical to the setup in Prystawski et al. (2024). Given that the main distinction between FTCT and the prior work is the introduction of spurious nodes (line 105-106), I would expect to see this prior work—which actually *did* introduce a novel learning task—given more prominent attribution.

- (Currently this work is referenced in Line 103—”The empirical findings of our work align with the observation in (Prystawski et al., 2024)…” The wording of this reference obfuscates the underlying causal structure that this prior work likely played in informing the current paper.)

**Generality:** The key findings of this paper are framed in very broad terms:

> “The emergence of compositional reasoning is highly influenced by the data’s relative knowledge ratio and model complexity. Specifically, a relative knowledge ratio of at least 0.3 and a Transformer architecture with at least two layers and two heads are critical for achieving this ability.” (Lines 520-523)
>

However, these conclusions are all drawn relative to one synthetic dataset with a highly-specific structure; it is unclear to what extent the empirical conclusions (e.g., compositional reasoning in transformers requires a relative knowledge ratio ≥ 0.3) generalize beyond the FTCT task. To make a convincing argument that these results have meaning beyond this one benchmark, this analysis ought to be replicated on more naturalistic reasoning benchmarks where few-shot CoT prompting is commonly used.

**Clarity:** The description of the FTCT dataset/task design (Sec. 3) fails to convey a clear description of the experiment setup and requires too much work of the reader. All aspects of prompt construction are described in excruciating formal detail, making it hard to separate design choices that are key to the experiment from implementation details. Overall, the formalism in this section is a barrier to understanding what’s going on at a more basic level.

- Fig. 1 lacks basic signposting needed to convey what is going on.
    - First off, there is no caption. This is a major omission as the figure is definitely not self-explanatory.
    - The blue highlights draw the reader’s attention to spurious features of the task (noise nodes) instead of the actual purpose of the task (predicting values of causal nodes).
- Other comprehension/clarity issues in Sec. 3:
    - “We assume op(e) represents operations like (+a) or (−b)” Does this mean addition/subtraction are the *only* possible operations?
    - I don’t understand how the merge operation works from the description.
    - Some unconventional choices of notation, such as using $f$ as an index over few-shot examples.
    - What is “downside processing” - do you mean “downstream”?

### Questions
1. Table 1 shows that all Transformer models attain 1.0 Values accuracy, even for small models that get very low Vertices accuracy. Can you account for this discrepancy?
2. An unintuitive pattern in the results (e.g., Fig. 2 and Table 3) is that accuracy *decreases* with the number of few-shot prompts $>1$. This results stands in contrast to a standard ICL setting, where inclusion of more examples typically improves performance. It is stated that this is “possibly due to increased dissimilarity between training and testing data with more CoT examples” (Line 277-278). Why does including more CoT examples causes the test data to be OOD? If this is the case, this seems like an important confound affecting this experiment setup that may not be adequately accounted for.
3. It is interesting to contrast the results from Sec. 5-6 with Zhang et al., 2022 (“On the Paradox of Learning to Reason from Data”), who apply a similar methodology but find that gradient descent fails to discover the correct $\theta^*$ for a logical induction task with very similar structure. Is there a reason why here the training succeeds at uncovering the underlying program, whereas in previous work it does not? More generally, it would be nice to see reference to this paper in the discussion.

### Soundness
3

### Presentation
2

### Contribution
3

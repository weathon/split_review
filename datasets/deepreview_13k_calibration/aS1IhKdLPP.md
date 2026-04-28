# Reflection Window: Text Generation with Selective Refinement

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
The autoregressive approach to text generation in large language models (LLMs), while widely used, is inherently suboptimal due to the lack of a built-in mechanism to perform refinement and/or correction of the generated content. In this paper, we consider optimality in terms of the joint probability over the generated response, when jointly considering all tokens at the same time. We theoretically characterize the potential deviation of the autoregressively generated response from its globally optimal counterpart that is of the same length. Our analysis suggests that we need to be cautious when noticeable uncertainty arises during text generation, which may signal the sub-optimality of the generation history. To address the pitfall of autoregressive text generation, we propose an approach that incorporates a sliding reflection window and a pausing criterion, such that reflection and generation can be carried out interchangeably as the generation proceeds. Our approach utilizes a selective refinement mechanism to strike the balance between efficiency and optimality, and the experimental results demonstrate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new decoding strategy called reflection window by using beam search at fixed generation window once detected conditional probability drop at specific position. Furthermore, the paper shows the effectiveness and efficiency of the proposed method compared with two baselines: greedy decoding and beam search on MMLU and MT-Bench with selected subsets.

### Strengths
1. The theoretical characterization of sub-optimality is reasonable.
2. The proposed method can be a potential solution for the gap between beam search and greedy decoding.

### Weaknesses
1. The experimental results are not convincing: 1) the selection of beam size and window size lacks justification, with no analysis about how these parameters are chosen or their impact on performance; 2) Only two baselines are used in the experiments while there are many speculative decoding methods that could provide a more comprehensive comparison; 3) the performance gap between greedy decoding and reflection window is too small in table 1, and there is no statistical significance test to validate the improvement.
2. There are a lot of cherry-picking implementation details: 1) the gap in STEM of MMLU is relatively bigger then the author chooses three subsets of STEM to conduct later experiments without revealing the reason and the performance on whole set. This selective reporting undermines the validity of subsequent conclusions; 2) table 2 shows there are only 100 test examples for MT-Bench, and there is no greedy decoding baseline included for comparison.
3. The necessity of reflection window is not clearly established, and there is a lack of comprehensive analysis, including the effects of beam size and window size on the whole set of MMLU and MT-Bench, as well as efficiency analysis. The absence of these analyses makes it difficult to assess the practical value of the proposed method.

### Questions
1. See above
2. Any human alignment results for MT-Bench since you choose LLM to judge ?
3. Why \sigma can be defined as shown in Eq(4) ?
4. One concern is about section 2.1. If we consider the attention distribution of LLMs, it is possible to let (b) become (a), I do not see the logic here and the proposed method also is auto-regressive method.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel technique for generation and reflection of LLM models. It utilizes a fast-slow pointer to maintain a slide window, where reflection tokens are generated. Generally speaking, the proposed method is quite interesting, and could be an easy strategy to implement. The proposed strategy would be able to balance the generation and reflection, and experimental results demonstrate its superior performance compared to greedy decoding and beam search.

### Strengths
1) Novelty in technique: Utilizing a fast-slow pointer for reflection and generation is quite a technically interesting idea for LLM decoding. 

2) Theoretical formalization is good to understand the problem of auto-regressive understanding.

### Weaknesses
1) Insufficient baseline methods: I think author should at least compare the proposed method with:
decoding algorithms: top-k/p sampling
Prompting based ‘reflection’ method and automatic post-editing strategy for fair comparison. 
Only comparing with beam/search decoding is insufficient.

2) Lack of Clear Demonstration on Distinction. Though an interesting idea, this paper does not highlight the difference between the proposed strategy with other reflection thinking strategies, practically or principally. Specifically, the paper does not clarify how the fast-slow pointer mechanism fundamentally differs from other methods that also aim to refine or correct generated text, such as those using iterative refinement or re-ranking techniques.

3) lack of logical necessity between the theoretical analysis and the proposed specific method. Despite the theoretical analysis provided in this paper, other methods are also applicable within this theoretical framework and can be viewed as specific cases under this analysis framework. Consequently, why propose a fast-slow pointer under such a framework instead of conventional approaches? Why is the proposed method superior under such an analysis framework? This paper does not answer those questions. The analysis does not provide a clear justification for the specific choice of a fast-slow pointer over other potential mechanisms that could also address the identified theoretical problem.

### Questions
Please refer to the weakness

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel generation technique that allows the LLM to pause autoregressive generation at one point and “reflect” over a window of the generated context, before resuming autoregressive generation. The authors formally show that autoregressive generation is suboptimal even with a good base LLM. Empirically, their approach operates by observing the entropy of previously generated tokens up to a certain window size, and if the entropy is above a certain threshold (indicating uncertainty) then generation is paused and beam search is used instead of greedy decoding. They evaluate their approach over MMLU and MT-bench, comparing it to greedy and beam search.

### Strengths
* The theoretical treatment of autoregressive sub-optimality is valid and interesting. 
* The authors did a good job highlighting a prevalent issue with current LLMs: The inflexibility of autoregressive word-by-word style generation.
* The proposed approach shows improvement over vanilla greedy decoding.

### Weaknesses
 * The authors refer to this approach as a "reflection/refinement" technique, but the refinement they refer to merely involves using beam search as opposed to greedy. In other words, the approach seems to me like a hybrid greedy/beam approach, rather than a refinement/reflection setup. While the idea of pause-and-reflect is very interesting, I find the execution to be very poor. Why not pause and run some refinement over the window (e.g., ask the LLM to revise the output) using a prompt-based approach, which could potentially leverage the LLM's understanding of the context for more meaningful revisions, instead of just relying on beam search?
* The whole approach is based on an assumption that the LLM is calibrated--and therefore an "oracle"---LLM, in the sense that highly likely sequences are correct/preferable. This motvates their assumption that beam search should serve as an approximation to globally optimal sequences. We know this is not the case, and LLMs are in many cases poorly calibrated. This can explain some results where beam search performs worse/on par with greedy decoding (such as in Table 3). In other words, the approach relies on a perfecly calibrated LLM, which may not be available. Furthermore, the use of entropy as a trigger for refinement is questionable, as high entropy could indicate a complex or nuanced part of the text that requires more creative generation rather than a simple beam search.
* Experimental results are not very convincing. Table 1 shows beam search to be better, and only 80 responses were used for evaluation on MT-bench. The lack of statistical significance testing further weakens the empirical claims. The limited scope of the experiments, focusing solely on MMLU and MT-bench, raises concerns about the generalizability of the findings to other tasks and datasets.
* The authors do not provide qualitative examples at all. I would be curious to see how this “refinement” process works, and how the rewritten parts eliminate mistakes and/or improves writing. It is crucial to understand the practical impact of this approach through concrete examples, especially given the claim of "reflection" and "refinement". Without qualitative analysis, it is difficult to assess the true value of the proposed technique.

### Questions
* After the refinement, what if the entropy condition still holds i.e., the newly generate tokens are also uncertain?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper targets to address a limitation of auto-regressive text generation in LLMs, where the process generates text token by token without refinement. They propose a novel method, reflection window, which allows the generation process to pause and reflect on previously generated tokens to correct errors when needed based on an entropy-based criterion. They focus on two benchmarks, MMLU and MT-bench and showed effectiveness compared to greedy decoding, obtaining scores comparable to beam search.

### Strengths
The proposed method, reflection window, is novel to address auto-regressive limitations since it includes self-correction in generation steps without generating full token sequences.

### Weaknesses
The pausing criterion's dependency on entropy threshold and window size means performance may vary with task and domain shifts. Therefore, it is necessary to consider diverse datasets with various generation tasks.

To demonstrate the robustness and effectiveness of the proposed method, more recent baselines for generation methods need to be considered.

Relying solely on automatic evaluation does not guarantee improvements in fluency, coherence, or error correction.

The paper specifically discusses a few decoder-only LLMs. Different types of models need to be evaluated for robustness.

### Questions
.

### Soundness
3

### Presentation
3

### Contribution
2

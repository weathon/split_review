# Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
As large-scale models evolve, language instructions are increasingly utilized in multi-modal tasks. Due to human language habits, these instructions often contain ambiguities in real-world scenarios, necessitating the integration of visual context or common sense for accurate interpretation. However, even highly intelligent large models exhibit significant performance limitations on ambiguous instructions, where weak reasoning abilities of disambiguation can lead to catastrophic errors. To address this issue, this paper proposes \textsc{Visual-O1}, a multi-modal multi-turn chain-of-thought reasoning framework. It simulates human multi-modal multi-turn reasoning, providing instantial experience for highly intelligent models or empirical experience for generally intelligent models to understand ambiguous instructions. Unlike traditional methods that require models to possess high intelligence to understand long texts or perform lengthy complex reasoning, our framework does not significantly increase computational overhead and is more general and effective, even for generally intelligent models. Experiments show that our method not only significantly enhances the performance of models of different intelligence levels on ambiguous instructions but also improves their performance on general datasets. Our work highlights the potential of artificial intelligence to work like humans in real-world scenarios with uncertainty and ambiguity. We will release our data and code.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Visual-O1, an approach that improves VLM's reasoning performance given ambiguous language instructions. For VLMs with stronger reasoning ability, the paper proposes an "instantial experience" approach where multi-turn multi-modal CoTs are generated to reason about the instruction, and the model subsequently directly outputs final answer conditioned on such reasonings. For VLMs with weaker reasoning ability, the paper proposes an "empirical experience" approach where after multi-modal CoTs are generated, explicit and clear instructions are generated before the model outputs the final answer. The authors demonstrate the effectiveness of their approach in referring image segmentation and visual question answering benchmarks.

### Strengths
- Context and instruction ambiguity is very prevalent in language and vision-language applications. Handling these cases is an important research problem. The proposed approach presents a promising way to improve the accuracy of VLM's "best guess reasoning" under ambiguous instructions.
- The paper is overall well-written, with clear methodology and extensive experiments.

### Weaknesses
 - Table 6 indicates that the effectiveness of the proposed approach and the results of the paper may be vulnerable to noise, and the improvements could lack statistical significance. Specifically, as the budget limit increases from 1 to 5, the success rates are "55.87, 54.16, 57.38, 55.27, 55.56," showing no clear trend of performance improvement with respect to budget limit. For instance, the fact that "budget limit = 3" outperforms "budget limit = 2" by 3% and "budget limit = 4" by 2% could simply reflect evaluation noise. This raises concerns about the robustness of the method, particularly whether the observed gains are consistent across different runs and datasets. The lack of a clear upward trend with increasing budget suggests that the method's performance might not scale predictably, and the reported improvements could be within the margin of error.
- The generated "clear instruction" in Figure 3 (which correspond to authors' "empirical experience" approach) appears to directly answer the initial question, rather than serving as an actual "instruction" that enables the LLM to explore various objects, select the relevant one, and then provide the final answer. Thus, authors' approach seems to undermine the purpose of an "instruction." For instance, for the ambiguous prompt `white bear turned slightly`, a more suitable instruction with ambiguity removed would be, `identify the bear that is predominantly white with subtle color variations from white`. The current approach seems to bypass the intended reasoning process by generating a direct answer rather than a guiding instruction, which limits the potential of the method to handle more complex ambiguous queries.

### Questions
- For stronger VLMs (e.g., GPT-4o), I don't quite get the motivation for authors to adopt the "instantial experience" approach instead of the "empirical experience" approach. Intuitively, allowing VLMs to reason and explicitly output the clear instructions with ambiguities removed should almost always improve their performance, regardless of the ability of the VLMs themselves. I also didn't find an ablation study in the paper to support why we need the "instantial experience" approach for stronger VLMs.
- Additionally, per my comments in the review, I'd encourage authors design better prompts such that the generated instructions in their "empirical experience" approach do not defeat the purpose of an actual "instruction".

### Soundness
2

### Presentation
3

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
This paper proposes Visual-O1, a multimodal multi-turn Chain-of-Thought reasoning framework to deal with ambiguous natural language instructions in two typical vision-language tasks: referring image segmentation and visual question answering. Visual-O1 builds
instance-specific experience for high-intelligence models or creates general experience for any ambiguous instructions for general-intelligence models. Experiments show that Visual-O1 improves the performance on both the ambiguous datasets and the general datasets.

### Strengths
1. This paper proposed a prompting method that seamlessly applies to both high-intelligence and general-intelligence models within the same framework. This adaptability indicates that Visual-O1 is not limited to a specific model type and can scale across different levels of model intelligence, which enhances its utility for a wider range of applications and users.
2. The authors presented extensive experimental results that include a variety of ablation studies and model comparisons. These results strengthen the credibility of their claims and provide thorough evidence of the framework's effectiveness. Notably, Visual-O1 not only improves performance on ambiguous instructions datasets but also enhances results on general datasets.

### Weaknesses
1. Although Visual-O1 shows clear improvements over baselines, the absolute success rates and IoU scores (on the ambiguity dataset) are still not entirely satisfactory. This gap suggests that there are underlying limitations to the model’s ability to handle certain types of ambiguous instructions. The paper could be strengthened if the authors provided a more detailed examination of failure cases (e.g., identifying specific patterns in instructions that remain challenging to disambiguate), including an analysis of whether these failures stem from limitations in the reasoning process itself or from the underlying segmentation or visual understanding capabilities of the model. Without this analysis, Visual-O1's readiness for real-world applications remains in question.
2. The paper tends to overemphasize its successes by frequently using terms like "significant," even when sometimes the improvements are marginal (e.g., success rate gains of less than 3%). This could be misleading, especially considering that the ambiguous instructions dataset is not large enough to robustly support such claims. Furthermore, the results do not report averages over different random seeds, which raises questions about the stability and generalizability of the improvements. It is essential to assess the variance in performance across multiple runs to ensure the observed gains are consistent and not due to random fluctuations.
3. Minor issues or typos: The term $x_\text{rsn}$ should be $x_\text{rfl}$ in Eq. (6). The word "botlle" should be "bottle" in Figure 3.

### Questions
1. Could you provide some further information to explain the difficulty of the ambiguous dataset? For example, how humans (might) perform on this dataset?
2. How are the Chain-of-Though and FuDD baselines implemented?
3. An example of $\mathcal{A}_\text{ins}$ is provided in the appendix. If I understand the method correctly, it should be composed of the alternating appearance of reasoning and reflection. Are the sentences in gray given by reflection? If so, is there an example of the full trajectory?
4. Analysis of Visual-O1's failure modes will help a lot, as discussed in the weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a method for visual o-1 that is similar to language o1 that increases the computation budget on test-time. The work is proposed to highlight the potential of artificial intelligence to work like humans in the real world, especially when the instruction is ambiguous for the instructional model. This is achieved by multi-turn reasoning with chain of thought. 

They have separated the multi-round reasoning process for high-intelligence model and general intelligent model, where it tends to have more round interaction when the model has a higher intelligence level.

They have evaluated their result on visual-QA, and RIS in comparison with the state-of-the-art model and shows reasonable improved on both segemtantion and visual-QA.

### Strengths
1. The paper's proposed direction of Visual-O1 towards instructional QA is an interesting direction.
2. By integrating the chain of thought into the pipeline, the model can improve the segmentation result of referring image segmentation, and the visual QA result. The performance gain on visual QA is larger than RIS, and the performance gain on ambiguous cases is higher than general cases, which indicates that the multi-round and multimodal inference needs more on the harder case.
3. The additional overhead of the visual chain of thought is limited for both training and evaluation stages.

### Weaknesses
1. To be completely honest, although the performance gain shows statistically significant improvement, however, the improvement is marginal, which indicates that the chain-of-thought works.
2. The author lacks examples when we actually need visual CoT (As the cipher example in o1).
3. As shown in Table.6, I actually think the budget curve is confusing, the performance fluctuates for Acc and BLEU, and saturate w/ 3 budget, this indicates that the designed algorithm is not sophisticated enough for scaling up.
4. They propose the empirical solution for less-intelligent model.

### Questions
1. Can you write the exact GPU settings for Table M?
2. How does the author interpret that the performance saturates quickly with the budget?

### Soundness
3

### Presentation
3

### Contribution
3

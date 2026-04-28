# Lean-ing on Quality: How High-Quality Data Beats Diverse Multilingual Data in AutoFormalization

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 6, 3, 3

## Abstract
Autoformalization, the process of transforming informal mathematical language into formal specifications and proofs remains a difficult task for state-of-the-art (large) language models. Existing works point to competing explanations for the performance gap. On one hand, large language models exhibit exceptional performance on translation tasks, suggesting their significant potential for autoformalization.  On the other hand, the quantitative reasoning capabilities of standard language models remain limited, leading to suboptimal performance on autoformalization and the subsequent task of formal theorem proving. To this end, we introduce a novel methodology that leverages backtranslation with hand-curated prompts to enhance the mathematical capabilities of language models, particularly addressing the challenge posed by the scarcity of labeled data.  Specifically, we evaluate three primary variations of this strategy: (1) on-the-fly (online) backtranslation, (2) distilled (offline) backtranslation with few-shot amplification, and (3) line-by-line proof analysis integrated with proof state information. Each variant is designed to optimize data quality over quantity, focusing on the high fidelity of generated proofs rather than sheer data scale. Our findings provide evidence that employing our proposed approaches to generate synthetic data, which prioritizes quality over volume, improves the autoformalization performance of LLMs as measured by standard benchmarks such as ProofNet. Crucially, our approach outperforms pretrained models using a minimal number of tokens. We also show, through strategic prompting and backtranslation, that our approaches surpass the performance of finetuning with extensive multilingual datasets such as MMA on ProofNet with only 1/150th of the tokens. Taken together, our methods show a promising new approach to significantly reduce the resources required to formalize proofs, thereby accelerating AI for math.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new method for the synthetic generation of informal/formal pairs and a method to improve model performance with significantly lower amounts of data than prior work. The authors show the performance of their generated data on ProofNet. The authors evaluate on-the-fly backtranslation, distilled few-shot backtranslation, and line-by-line proof analysis with the complete proof state.

### Strengths
- The authors propose a new methodology.
-

### Weaknesses
 - ProofNet Test is the only evaluation performed, so generalizability is hard to see.
- Without multiple evals, the risk of data contamination with ProofNet is high, but the paper did not address this.
- The only model trained was GPT-2 124M, and as the authors addressed, performance could be better for larger models. There was no investigation into the scaling laws of this approach.
- There was no analysis of the types of proofs that the method performs well at; for example, there could be a subset of categories in which the generations are good and some in which they are poor.

### Questions
- How does the dataset impact performance on other datasets?
- How does fine-tuning a larger model impact performance?
- What is the evidence that there is a high likelihood that this approach scales?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new dataset by translating a formal proof back to its informal description. It proposes three methods to generate the dataset: the first is to train the base model to generate the informal statement and translate it back to the original formal statement. The second uses GPT-4 to obtain the informal data given the formal one. The third applies templates to convert formal language into informal. Experimental results show that the GPT-2 trains on the GPT-4 generated data can obtain lower eval loss than the previous dataset.

### Strengths
The idea of using back-translation to obtain more informal-formal data sounds reasonable. The technique has been shown effective in translation tasks and thus has potential in the auto-formalization field.

### Weaknesses
 - The experiments are weak. Among all proposed generation methods, only the GPT-4 generated achieves better eval loss than previous data. Also, to verify the effectiveness, the authors should compare with an existing autoformalization method before and after using the proposed AI4Math dataset.

- The paper does not give examples of the generated data. The templated-based generation method does not show how to translate a formal statement to an informal one, which is a very difficult and important part of autoformalization.

### Questions
Why use eval loss to assess autoformalization performance?

Overall, the paper has limited novelty and does not have sufficient experiments to validate the effectiveness of the proposed method. The author needs to show the extra data can improve current SOTA LLMs in terms of auto-formalization pass rate. Thus I lean towards rejection but look forward to the authors' reply with stronger results, better baselines, and more ablation studies.

### Soundness
2

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
5

### Summary
The paper explores the challenges in autoformalization, the process of translating informal mathematical statements into formal proofs, particularly for language models. Recognizing the limitations of large models in handling complex mathematical reasoning, the authors introduce a method that leverages backtranslation with curated prompts to improve data quality over volume. They propose three main techniques: on-the-fly backtranslation, offline distilled backtranslation with few-shot amplification, and a line-by-line proof analysis integrated with proof state information. The authors argue that prioritizing high-quality, task-relevant data can improve model performance significantly, as demonstrated by their experiments on the ProofNet benchmark. They achieve notable improvements using fewer tokens than comparable multilingual datasets, emphasizing quality over quantity. The paper contributes to the autoformalization field by demonstrating that a focus on data fidelity can reduce computational costs while enhancing model effectiveness.

### Strengths
- The paper introduces a novel methodology focused on enhancing data quality through backtranslation and curated prompts, effectively addressing the scarcity of high-quality labeled data in autoformalization.

- By demonstrating that high-quality data can outperform large multilingual datasets, the paper shows an effective way to reduce computational resources while achieving superior performance, which is particularly valuable for resource-constrained settings.

- The authors test three variations of their approach (on-the-fly, distilled backtranslation, and line-by-line proof analysis), offering a well-rounded examination of data generation methods that optimize model training and performance.

- The method achieves substantial improvements on the ProofNet benchmark, indicating that a high-quality data approach can effectively bridge some of the performance gaps in autoformalization tasks without requiring extensive multilingual data.

- This work provides a valuable perspective on the importance of targeted data in autoformalization, suggesting new directions for developing efficient and effective models for translating informal mathematical language into formal proofs.

### Weaknesses
 - The experiments are primarily conducted using GPT-2 due to resource constraints, which may limit the generalizability of the findings. The performance could vary significantly with larger, more capable models, so additional testing on models beyond GPT-2 would provide a more comprehensive evaluation. Specifically, the paper does not explore how the backtranslation method scales with models that have different architectures or pre-training objectives, which could significantly impact the quality of the generated data and the final performance.

- While the paper demonstrates improvements on the ProofNet benchmark, it lacks discussion on how well the method generalizes to diverse or real-world mathematical texts beyond curated datasets. Including a broader evaluation on real-world examples would strengthen the applicability and robustness of the approach. The current evaluation focuses on a controlled environment, and it is unclear how the model would perform when faced with the variability and ambiguity inherent in real-world mathematical language, which often includes less structured and more nuanced expressions.

### Questions
- Could you provide more experiments on datasets like MiniF2F[1]?
- I would like to know if this method is generalizable to any formal language. Could you provide results on theorem provers like Metamath?

**Reference:**  
[1] Minif2f: a cross-system benchmark for formal olympiad-level mathematics

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper advocates to use backtranslation with hand-crafted prompts to generate high-quality formal language (Lean) and natural language pairs to alleviate the data scarcity issue, thus improving the autoformalization capability of LLM, an important yet unsatisfying capability of current LLMs. Specifically, it evaluates three methods, i.e. online backtranslation, offline backtranslation, and line-by-line proof analysis with proof state information. The resulting synthetic dataset on autoformalization, AI4Math, improves the autoformalization performance of LLMs as measured by standard benchmarks such as evaluation loss on ProofNet.

### Strengths
The paper mentions several useful tricks. For example, the three approaches: online and offline backtranslation, line-by-line proof analysis.

### Weaknesses
 * All the proposed techniques read familiar with previous arts

Backtranslation (or informalization) is a well-known practice in the field of NLP and autoformalization. For example, ProofNet also used a distilled backtranslation technique for autoformalization. The proposed online and offline methods do not seem to provide sufficient additional knowledge to the community, compared to previous works in this regard. And the line-by-line proof analysis reads similar to "Let's verify step by step" from OpenAI, which resembles a process reward modeling (PRM) approach. The three take-aways, quality over quality/diversity, intermediate steps matter, are all basically derived from the previous work and are now well-known before this paper submission.

* Insufficient results demonstrating the effectiveness of the techniques

A critical problem of this paper is to use eval loss (table 2) to demonstrate the effectiveness of autoformalization. An autoformalization should be checked manually or by some symbolic engine (Lean) with metrics like pass@10. As a matter of fact, eval loss is no longer a reliable metric to reflect the quality of an LLM. The current practice to test more end-to-end tasks (e.g., MMLU) to evaluate LLMs. Moreover, the effectiveness of a technique on weaker models (e.g., GPT-2) does not necessarily imply gains on superior models (Lemma or Llama 3-7b). It is generally harder to improve an LLM whose quality is already very good. Also, some baseline selected in this paper, such as MMA is weak. MMA is not yet considered a strong baseline (rejected by ICLR'24).

### Questions
* Please justify the methodology (eval loss) used to demonstrate the effectiveness of autoformalization. 
* Please clarify the novelty of the proposed technique, compared to previous work.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper titled **"LEAN-ING ON QUALITY: How High-Quality Data Beats Diverse Multi-lingual Data in Autoformalization"** presents a novel approach to improving autoformalization in theorem proving by leveraging high-quality, carefully curated training data over larger, more diverse datasets. The authors propose a methodology using backtranslation with three key variations: on-the-fly backtranslation, distilled backtranslation with few-shot prompting, and line-by-line proof analysis. The paper evaluates these approaches on the ProofNet benchmark, demonstrating that using fewer but higher-quality tokens can significantly enhance large language models' (LLMs) performance in autoformalizing mathematical statements into formal languages like Lean4.

### Strengths
- The experiments are well-designed, with clear results showing that the proposed methods outperform existing approaches like the MMA dataset, even with significantly fewer tokens. 

- While the overall structure is clear, certain sections, such as the methodology and dataset examples, could be more accessible to a broader audience.

### Weaknesses
 - **Limited Exploration of LLMs** While the paper demonstrates promising results using GPT-4 for informalization and GPT-2 for fine-tuning, it would benefit from a broader exploration of available language models, especially those specialized in formal mathematics:

  1. **Comparison with Gemini-Pro**: Recent findings from the Lean community suggest that Gemini-Pro may be more adept at handling formal language tasks. Comparing GPT-4's performance to Gemini-Pro in the informalization process could provide deeper insights into the strengths and weaknesses of both models in this context.

  2. **Scaling beyond GPT-2**: The paper primarily relies on GPT-2 for fine-tuning. Given its relatively small size and age, this choice may not fully showcase the potential of the proposed methodology. Testing more advanced models (e.g., including SwiGLU into FFN) could offer a clearer understanding of how well the approach scales and performs with larger models. Were there specific reasons (e.g., computational constraints or model availability) for selecting GPT-2 over newer or larger models?

  3. **Evaluation of Formal Mathematics Models**: The study does not examine models specifically designed or fine-tuned for formal mathematics, such as Llemma-7B, Qwen-math, and DeepSeek-math. By focusing on smaller, more general-purpose models, the paper leaves open questions about scalability and effectiveness when applied to larger, more specialized models. Incorporating experiments with these models, which include formal language in their pretraining data, would provide stronger evidence of the method's generalizability and its potential across different model architectures and sizes.

- **Lack of Relevant Works**:  While the paper compares its methods primarily against the MMA dataset, it overlooks several other key works that are crucial to the domain of autoformalization. These include Lean Workbook, Forml4, ProofNet, and FIMO. Including a comparison with these datasets and approaches would provide a more robust evaluation and a clearer understanding of how the proposed methodology fits into the broader landscape of autoformalization research.

  To strengthen the paper, I suggest adding a brief comparison table or a discussion that highlights the key differences and similarities between your method and these other works. Specifically, it would be valuable to explain how your approach addresses limitations or advances beyond these existing methods. Additionally, focusing on aspects such as dataset complexity, formal language coverage, or model performance metrics (e.g., accuracy, generalizability, or scalability) would allow for a more meaningful and detailed comparison.

  Incorporating this discussion would significantly enhance the clarity and depth of the evaluation, positioning the proposed methodology more effectively within the current state of the field.

- **Insufficient Examples**: The paper would benefit from including more concrete examples that showcase the effectiveness of backtranslation in autoformalization. Providing specific before-and-after examples from the AI4Math dataset would help clarify the practical advantages of the approach. Additionally, offering more detailed dataset examples would enhance the readers' understanding of the datasets used, offering a clearer and more thorough view of the challenges and types of problems being addressed.

- **Cost Analysis**: While the paper mentions cost limitations for dataset generation, a more detailed cost analysis of each backtranslation method (in terms of time and resources) would provide valuable insights for scaling these techniques.

- **Unconvincing Metrics**: Cross-entropy loss alone is insufficient for evaluating autoformalization performance, as it primarily measures token-level differences and does not account for the full complexity of translating informal to formal languages. Autoformalization often allows for multiple valid formal expressions that correctly align with the same informal statement. In datasets like MMA, human experts are typically involved in verifying the alignment between formal and informal languages, highlighting the need for more robust evaluation methods.

  A more effective approach would be to evaluate autoformalized statements and their corresponding proofs by passing them through a Lean4 compiler. Successfully compiled proofs would indicate strong alignment with the original informal statements, as seen in prior work. This method could provide a more reliable assessment of the correctness and coherence of the autoformalized outputs.

  To strengthen the evaluation, I suggest incorporating additional metrics beyond cross-entropy, such as the compilation success rate in Lean4, which would better capture the semantic accuracy of the autoformalization process. If the Lean4 compiler has not been used, it would be helpful to understand the challenges that the authors foresee in implementing this approach. Additionally, exploring other metrics, such as proof-checking accuracy or formal consistency from human experts, would provide a more comprehensive picture of how well the autoformalization aligns with formal proof standards.

  Incorporating these evaluation methods would offer a more nuanced understanding of the proposed model's performance and its ability to handle the complexities of translating informal statements into formal proofs.

### Questions
- Could the authors provide more concrete examples of autoformalization tasks handled by the proposed methods? How do these examples compare to the baseline methods in terms of complexity and performance?
- Have the authors explored incorporating human-in-the-loop feedback during the informalization process? If so, how does it impact the quality of the final autoformalized proofs?

### Soundness
2

### Presentation
2

### Contribution
2

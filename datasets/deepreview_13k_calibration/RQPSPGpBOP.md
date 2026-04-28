# Can a Large Language Model be a Gaslighter?

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
[Warning: Some examples in this paper could contain objectionable contents.]
Large language models~(LLMs) have gained human trust due to their capabilities and helpfulness. However, this in turn may allow LLMs to affect users' mindsets by manipulating language. It is termed as gaslighting, a psychological effect. 
In this work, we aim to investigate the vulnerability of LLMs under prompt-based and fine-tuning-based gaslighting attacks. Therefore, we propose a two-stage framework DeepCoG designed to: 1) elicit gaslighting plans from LLMs with the proposed DeepGaslighting prompting template, and 2) acquire gaslighting conversations from LLMs through our Chain-of-Gaslighting method. The gaslighting conversation dataset along with a corresponding safe dataset is applied to fine-tuning-based attacks on open-source LLMs and anti-gaslighting safety alignment on these LLMs. Experiments demonstrate that both prompt-based and fine-tuning-based attacks transform three open-source LLMs into gaslighters. In contrast, we advanced three safety alignment strategies to strengthen~(by $12.05\%$) the safety guardrail of LLMs. Our safety alignment strategies have minimal impacts on the utility of LLMs. Empirical studies indicate that an LLM may be a potential gaslighter, even if it passed the harmfulness test on general dangerous queries.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates a specific type of vulnerability in LLMs — gaslighting. The authors propose a framework for generating gaslighting conversations to explore this issue. Using this framework, they create an evaluation dataset comprising various gaslighting attacks, as well as a safety alignment dataset for defense purposes.

### Strengths
* This paper investigates a novel type of vulnerability in LLMs — gaslighting. The study provides valuable insights into the sources, harmfulness, and potential defenses against this issue.
* The collected datasets are a useful resource for the community, aiding further study of gaslighting problems and contributing to advancements in model safety.

### Weaknesses
 * The prompt-based attack appears to be ineffective on models with general safety alignment, such as ChatGPT and LLaMA2-Chat. This raises concerns about the significance of the gaslighting problem. If previous general safety alignment techniques and safeguards already mitigate this specific attack, then focusing on gaslighting as a unique threat may be unnecessary.
* The finetuning-based attack seems impractical in real-world scenarios. It is unlikely that a model developer would use primarily harmful data to train a model. In a realistic setting, the assumption should be that an attacker can only poison a small subset of data. Therefore, it is essential to demonstrate the effectiveness of this attack under a low poisoning rate.

### Questions
See weaknesses.

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
The paper studies whether LLMs could be gaslighters, which means LLMs affect users’ mindsets by manipulating language. The paper builds a gaslighting conversation dataset along with a corresponding safe dataset. The authors then implement prompt-based, fine-tuning-based gaslighting attacks and anti-gaslighting safety alignment with the datasets.  Experiments show that both prompt-based and fine-tuning-based attacks turn LLMs into gaslighters, while safety alignment strategies can strengthen the safety
guardrail of them.

### Strengths
1. The research question of how LLMs could affect people's mindsets is interesting and important.
2. The proposed datasets and curation methods are sound and novel.
3. The experiments are comprehensive and can support most of the claims.

### Weaknesses
1. Measuring the degree to which the LLM gaslights the user is the basis of the entire experiment. However,  the designed metrics and scales lack an explanation
2. how the human annotators were recruited and worked is not clear. Since all the results need the human annotation results to justify, adding more clarifications, or recruiting more annotators (e.g. from online platforms) and calculating metrics such as IAA will strengthen this part.


3. How the attacks could affect the general abilities of LLMs is not studied.

### Questions
1. Did the 2 annotators annotate all the 248 examples separately? Is this too much workload to guarantee the results are of high quality?

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
4

### Summary
The paper investigates the potential for large language models (LLMs) to engage in gaslighting, a form of psychological manipulation. The authors propose a framework called DeepCoG, which includes a two-stage process: DeepGaslighting, to create gaslighting plans, and Chain-of-Gaslighting(CoG), to generate conversations demonstrating gaslighting.

### Strengths
The topic of psychological manipulation via LLMs is both novel and critical, as LLMs become more integrated into daily life.

The use of various psychological metrics to assess gaslighting effects on users’ mental states is a valuable addition to the evaluation.

The paper includes helpful visual aids, such as clustering distributions and radar charts, to clarify findings.

### Weaknesses
 The paper’s reliance on GPT-4 for scoring gaslighting may introduce biases inherent in GPT-4’s design.

The framework and attacks, while effective, are largely adaptations of existing techniques, which might limit the novelty.

While the study simulates user interaction, real user behaviors in response to gaslighting were not part of the experiment.

### Questions
1. In a real-world setting, users often engage in extended dialogues with LLMs over time. How does the anti-gaslighting alignment fare in extended interactions, where gaslighting prompts or manipulative tendencies may emerge gradually rather than in a single interaction? Could the model’s resistance diminish or remain stable in conversations spanning numerous turns?

2. Given that the safety alignment strategies (S1, S2, S3) rely heavily on specific datasets and psychological constructs, how would these methods generalize to LLMs trained on different cultural contexts or language backgrounds? What adaptations would be necessary to ensure effectiveness in a broader linguistic and cultural scope?

3. Gaslighting and constructive feedback may sometimes appear similar (e.g., highlighting personal flaws). How does the proposed model differentiate between harmful manipulation and well-intentioned guidance? Would there be a risk of the model overcorrecting and limiting legitimate constructive feedback?

4. The study uses GPT-4 for scoring responses on gaslighting potential. To what extent can we rely on such automated scoring without introducing biases from GPT-4’s own training data? Would human evaluations provide more reliable insights, especially on nuanced psychological metrics, and how might these evaluations vary from GPT-4's?

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
The paper examines whether Large Language Models (LLMs) can perform gaslighting, a manipulative behavior that causes users to doubt themselves. The authors introduce DeepCoG, a framework that generates gaslighting conversations by identifying and applying manipulation strategies from LLMs. They show that models like Llama2, Vicuna, and Mistral can be turned into gaslighters through specific prompt-based and fine-tuning attacks. To prevent this, the study proposes three safety alignment techniques that increase the models' resistance to gaslighting by 12.05% while maintaining their effectiveness. The research also finds that traditional toxicity detectors fail to recognize gaslighting content, underscoring the need for specialized safety measures to ensure LLMs promote user well-being.

### Strengths
- The authors provides with a very strong framework in exploring gaslighting as a form of attack for LLMs which have significant potential in future research
- The experiments were well designed and explains clearly the effect of gaslighting as an attack as well as their solution towards gaslighting as an attack

### Weaknesses
 - There should be a human evaluation on how humans are able to gaslight in compare with GPT4o generated gaslighting to show a performance difference
- The author stated that the emotion might affect the defense of "users" but should do furthur analysis on how the effect is through abalation studies
  - How does emotion affects gaslighting efficency
  - What happens when we have a mixture of emotions when being gaslighted
  - The test have also been focusing solely on the effect of negative emotions- how about positive ones?
- Figure 4 is confusing might be better shown with a table, and should also contain a baseline (no attack) to compare with 
- Too much abbreivation within the paper- please try to reiterate key terms when refer again in the later paper like MD PO
- Missing citations- For example, previous work that utlizes gaslighting for improving LLM performance: https://www.ijcai.org/proceedings/2024/0719.pdf

### Questions
-  Does system prompt injection helps dealing with gaslighting? i.e. "Please be aware of gaslighting"
- How does emotion affects gaslighting efficency
- What happens when we have a mixture of emotions when being gaslighted
- The test have also been focusing solely on the effect of negative emotions- how about positive ones?

### Soundness
3

### Presentation
2

### Contribution
2

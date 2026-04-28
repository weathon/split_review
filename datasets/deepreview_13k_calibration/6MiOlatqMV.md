# MathCAMPS: Fine-grained Synthesis of Mathematical Problems From Human Curricula

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Mathematical problem solving is an important skill for Large Language Models (LLMs), both as an important capability and a proxy for a range of reasoning abilities.
    Existing benchmarks probe a diverse set of skills, but they yield aggregate accuracy metrics, obscuring specific abilities or weaknesses. 
    Furthermore, they are difficult to extend with new problems, risking data contamination over time.
    To address these challenges, we propose MathCAMPS: a method to synthesize high-quality mathematical problems at scale, grounded on 44 fine-grained ``standards'' from the Mathematics Common Core (CC) Standard for K-8 grades. We encode each standard in a formal grammar, allowing us to sample diverse symbolic problems and their answers. We then use LLMs to realize the symbolic problems into word problems. We propose a cycle-consistency method for validating problem faithfulness. Finally, we derive \emph{follow-up questions} from symbolic structures and convert them into follow-up word problems---a novel task of mathematical dialogue that probes for robustness in understanding. Experiments on 23 LLMs show surprising failures even in the strongest models (in particular when asked simple follow-up questions). Moreover, we evaluate training checkpoints of Pythia 12B on MathCAMPS, allowing us to analyze when particular mathematical skills develop during its training. Our framework enables the community to reproduce and extend our pipeline for a fraction of the typical cost of building new high-quality datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method called MathCAMPS to create mathematical problems grounded in a set of standards set by the Mathematics Common Core from kindergarten through 8th grade. The approach begins by converting each standard into a formal grammar which enables sampling symbolic problems from the grammars with their corresponding answers. 

A large language model (LLM) is then used to translate these symbolic problems to math word problems with a cycle-consistency check ensuring that the generated problems are both coherent and faithful. Since the values symbolic problems can be modified the authors also test the robustness of existing models with followup questions (including incremental or counterfactual variations). 

The paper includes the release of 9607 problems along with the framework to generate additional ones, and evaluate several of existing language models using this dataset.

### Strengths
The paper is clear and well-structured. It introduces a novel approach and provides the framework to generate mathematical reasoning problems using Mathematics Common Core Standards. The flexibility of this approach allows for synthesizing followup question which is used to test the robustness of an extensive list of large language models. 

The paper also analyzes checkpoints of Pythia 12B model during pretraining for learning dynamics of mathematical skills.

The extensive evaluation, which includes testing existing models on the dataset and analyzing model performance across different grade levels shows a through and high quality investigation. The paper provides valuable insights into the varying reasoning capabilities of existing LLMs and highlighting significant disparities in their performance.

### Weaknesses
While the paper presents extensive evaluations, it often falls short in providing detailed insights or intuitive explanation for the more surprising failures or performance gaps observed in some models. For instance, "surprising failures and gaps in performance" is mentioned twice in the abstract and the intro without much information. A deeper analysis of these areas would offer a richer understanding of the challenges and areas of potential improvement.

In my opinion, Figure 1 should be on page 3 or closer to the reference on page 4 where the method is being discussed. This would improve the flow of the paper and prevent the readers from having to constantly flip back and forth.

A potential limitation of the cycle consistency check is whether it is sufficient on its own. It only verifies the reproduction of the rules, but it does not account for intermediate consistency or potential intermediate issues in the generation. The imperfections of this cycle-consistency check could potentially remove good questions. 

The framework only covers 44 reasoning behaviours, with some being very basic and "easy" for current models. This seems relatively low given the complexity of mathematical reasoning. Generating thousands of problems based on just 44 rules seems somewhat repetitive and may limit the diversity of the problems produced. 
Higher grades could potentially include and require skills related to lower grades. This could potentially increase the redundancy of generated samples. 

The analysis of the follow-up questions appears to be somewhat superficial and lacks depth in exploring the models' performance and reasoning. The counterfactual questions, in particular, lack control over how the LLM generates the modified question, potentially leading to questions that can be solved independently of the original problem.

### Questions
the paper mentions "Prompting the LLM to back-translate the word problem into a symbolic structure and comparing the new answer to the original enables us to eliminate most unfaithful generation errors and maintain high quality." Could you provide some examples of these unfaithful generations? This would help better understand the soundness of the approach. 

As mentioned previously, is the cycle consistency sufficient? as it is only checking for the rules and not the intermediate descriptions? Relying solely on the model for back-translation could introduce imperfections, as a strong model might overlook errors in the math word problems and still produce a correct symbolic problem. Or the model might fail to properly adhere to the question's theme, resulting in an awkward or poorly aligned problem.

How do you validate counterfactual follow-ups when modifying variables with fixed limits, such as the number of days in a week or months in a year?

Given that only 44 rules are used to generate thousands of problems, could this limit diversity? How many training examples are needed to effectively learn these 44 rules? I think this experiment is worth studying to assess the quality of the generated examples.

Doesn't a higher grade level inherently include the skills required at lower grade levels?
Also, Shouldn't the average of the levels be weighted instead of uniform over different levels as K level questions are much simpler than 8th grade?

In the counterfactual setting, the second question seems to be merely a variation of the first, with a different value for the variable. How can this truly be considered a "follow-up" if the questions are independent and don't rely on each other? Could these questions not be solved independently?
Did you try just querying the model with the modified question? seems like the old problem and solution serves as a distraction here for the model and not providing much information?

The paper mentions "mathematical dialogue is much less frequent in pre-training data". Not entirely sure if this is true, but most models are instruction tuned and aligned with dialogue data during post-training. Do you think the follow-up setup truly constitutes a mathematical dialogue setup? Since there are only 2 turns.

What is the distribution of 44 skills/standards over classes from k to 8th grade?

"How do mathematical skills develop during pre-training?" This is an interesting question, but how does instruction tuning factor in, given that most current models are fine-tuned/instruction-tuned for this purpose?

Here are some suggestions: 
Citations could be removed in Table 1. This is artificially increasing the length. 
Figure 2 legends can benefit from a brief description of what each standard means to help readers better interpret the figure.

### Soundness
3

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
4

### Summary
The paper "MATHCAMPS: Fine-Grained Synthesis of Mathematical Problems from Human Curricula" presents a novel approach to generating mathematical problems that align with educational standards, specifically the Common Core. The authors introduce a pipeline that synthesizes symbolic problems, generates follow-up questions, and translates these into natural language, enhancing the interaction between LLMs and mathematical reasoning tasks.

Key contributions of the paper include:

- Problem Generation Framework: The authors develop a method to create high-quality mathematical problems based on established curricula, addressing the challenge of data contamination in existing benchmarks.

- Cycle Consistency Validation: A unique cycle-consistency check is proposed to ensure the faithfulness of the generated problems, enhancing the reliability of the evaluation process.

- Follow-Up Question Integration: The study emphasizes the importance of follow-up questions in assessing the robustness of LLMs, revealing significant performance drops when models are required to handle these additional queries.

Overall, the paper contributes to the understanding of mathematical reasoning in LLMs and provides a framework for future research in generating and evaluating mathematical problems.

### Strengths
- This paper investigates a critical topic: how to synthesize test sets in order to reduce the risk of leakage associated with publicly available test sets in large model training.

- The MathCAMPS test set, designed based on the Mathematics Common Core Standards for K-8 grades, allows for a fine-grained assessment of models' mathematical reasoning abilities, which is highly significant.

- The designed mathematical dialogue and cycle-consistency check are sensible.

### Weaknesses
 - The synthesized problems depend on the capabilities of GPT-4. If the questions are particularly difficult, such as those on the AIME, this framework may fail due to insufficient synthesis model capabilities. However, manually designed questions can mitigate this issue.

- MathCAMPS is only compared to GSM8K, which is insufficient, as GSM8K contains only simple elementary algebra problems.

- It cannot be guaranteed that the synthesized mathematical problems are always reasonable or that the answers will consistently match.

### Questions
- When sampling different questions, the model's performance is expected to show subtle variations. The authors should sample multiple test sets to assess the variance in the model's performance.

- The authors should discuss how the framework can be extended when we need to synthesize more complex problems.

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
3

### Summary
This paper presents MathCAMPS, a framework for the fine-grained synthesis of mathematical problems based on human curricula. It employs a symbolic-based approach to generate scalable evaluation data for models. The authors introduce a cycle-consistency method to validate the faithfulness of the generated problems. Additionally, they conduct a series of experiments to validate existing models on the proposed benchmark.

### Strengths
1. The motivations of this paper are well-founded: 1. Preventing data contamination 2. Providing fine-grained evaluation.
That's exactly the problem that cannot handled by existing mathematical benchmarks.

2. The pipeline proposed by the authors effectively addresses the identified challenges. In particular, the cycle-consistency is novel and solid, significantly enhancing the quality of the generated data.

3. Furthermore, the experimental section of the paper is comprehensive and offers valuable insights.

### Weaknesses
1. While the proposed method demonstrates a degree of scalability, it is primarily limited to K-8 level mathematics. The experiments conducted in this study show a strong consistency with evaluations from the GSM8K benchmark. However, I don't think as more powerful models, such as OpenAI's o1, emerge, this benchmark will present significant challenges. Therefore, the potential for extending this framework to more complex problems is a key area for improvement in this work.

2. Additionally, the paper's heavy reliance on the Common Core (CC) standards results in an inability to generate mathematical problems outside of these guidelines. Consequently, more complex problems (those above K-8) or those that fall within K-8 but are not included in the CC standards cannot be synthesized.

### Questions
1. How does the author ensure the correctness of encoding the CC Standard into rules? Did the author conduct manual cross-validation or sampling tests?

2. Are there any methods to extend this pipeline to more difficult topics?

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
4

### Summary
This paper introduces a scalable approach for generating high-quality synthetic mathematical problems. The process begins by using a math standard to develop a formal grammar, which is used to sample symbolic problems with answers. These symbolic problems are then transformed into word problems using large language models (LLMs). A cycle-consistency method validates the faithfulness of the generated problems. Additionally, follow-up questions derived from symbolic structures are transformed into word problems, creating a new type of mathematical dialogue task to assess understanding robustness. Extensive evaluation shows that even advanced models struggle with follow-up questions. The paper also analyzes the development of specific mathematical skills by using different training checkpoints of the Pythia 12B model.

### Strengths
- MathCAMPS Benchmark: The proposed MathCAMPS benchmark is precisely aligned with the K-8 Mathematics Common Core (CC) Standards, enabling a comprehensive evaluation of mathematical skills. This structure supports a detailed analysis of proficiency exhibited by Large Language Models (LLMs) across specific mathematical reasoning capabilities.

- Grammar-Based Skill Encoding: By encoding CC skills in a structured grammar (symbolic representation), MathCAMPS can generate a wide array of targeted problems that address specific skills, such as decimal addition or solving equations with fractions.

- Cycle-Consistency Validation: MathCAMPS employs a cycle-consistency method to confirm that word problems accurately represent their original symbolic counterparts. By prompting the language model to translate a word problem back into symbolic form and then comparing results, this method effectively reduces misrepresentation and enhances problem fidelity.
- Mathematical Dialogue for Enhanced Understanding: MathCAMPS introduces two types of “mathematical dialogue” tasks to probe deeper understanding.
   -- Counterfactual Questions: These questions modify aspects of the original problem, testing the model's adaptability to new conditions.
Incremental Questions: These questions add information to the problem, requiring the model to integrate prior context with new details.
   -- Incremental Questions: These questions add information to the problem, requiring the model to integrate prior context with new details.

However, apart from using CC standards and dialog setting, the novelty of the work is low.

### Weaknesses
This work has gone in a similar direction as many papers, where researchers have looked back at the progress of math reasoning and found that substantial progress has not been achieved as claimed by tall IMO claims.  For example recently [1] found a way to synthetically generate symbolic math dataset with controlled perturbations, train and test some BERT based models and also benchmark SOTA LLMs.  Previously the type of inconsistency was done  by [3] where authors showed that vanilla transformers can not multiply numbers while [2] showed success in solving integrals. 
While these papers are mostly symbolic problems without much of natural language, other work, such as GSM-Symbolic [3], MORE [4] has provided a vast coverage of different variations that probes the robustness of arithmetic reasoning abilities. MORE provides a vast ontology of perturbations and GSM-symbolic provides many useful templates. Also, while GSM-symbolic is fairly recent, MORE has been published many months back. Given the similarity, it should be mentioned and compared with.

Unfortunately, the paper therefore is not as novel as it claims to be. Other than utilizing CC standards and the dialog setting, contributions are questionable.
More questions:
1. How faithful is the representation from CC NL guidelines to the formal grammar? Have the authors evaluated this step independently?
2. LLM generations are evaluated/flitered using cycle consistency. How did you filter our hallucinations, other errors? Again, what is the comparison with MORE?

The insights from training Pythia feels much more interesting than the other parts of the paper, though it consitutes a small body of the entire work.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

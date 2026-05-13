# MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning

- Decision: Accept
- Scores: 8, 8, 8, 6, 6

## Abstract
We introduce \model,  a series of open-source large language models (LLMs) specifically tailored for general math problem-solving. The \model models are trained on \dataset, our meticulously curated instruction tuning dataset. \dataset is compiled from 13 math datasets with intermediate rationales, six of which have rationales newly curated by us. It presents a unique hybrid of chain-of-thought (CoT) and program-of-thought (PoT) rationales, and also ensures extensive coverage of diverse fields in math. The hybrid of CoT and PoT not only unleashes the potential of tool use but also allows different thought processes for different math problems.  As a result, the \model series substantially outperform existing open-source models on nine mathematical reasoning datasets across all scales with an average accuracy gain between 16\% and 32\%. Remarkably, our \model-7B model reaches 33\% on MATH (a competition-level dataset), which exceeds the best open-source 7B model (WizardMath) by 23\%, and the \model-34B model achieves 44\% accuracy on MATH, even surpassing GPT-4's CoT result. Our work underscores the importance of diverse problem coverage and the use of hybrid rationales in developing superior math generalist models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a MathInstruct dataset to improve the general performance of all types of math problems.
Specifically, they annotate public datasets with CoT and program-of-thought (PoT) annotations with GPT-4.
Through experiments on many in-domain and out-of-domain datasets, they demonstrate the effectiveness of this dataset.

### Strengths
1. Expensive efforts in creating the dataset, very valuable if provided to the research community. 
2. Performance improvements over the baseline approaches without the MathInstruct dataset

### Weaknesses
1. I actually train a 7B-CodeLLaMA with GSM8K0PoT training set prompted from GPT-3.5-turbo myself, the performance can definitely achieve 62% (>59.4 in Table 3). I'm not sure what would be the quality of this dataset. I'm not sure if the authors are aware that the performance of CodeLLaMA trained on GSM8K PoT can achieve such performance. I'm also not sure whether the authors have tried to train CodeLLaMA with other datasets in MathInstruct, such as MATH dataset. I don't mind sharing my GSM8k training set for the authors to reproduce. 
2. In other words, I think the author should have more experiments to justify the datasets. For example, GSM8K PoT, we need to compare with a CodeLLaMA that trained on GSM8K PoT training set. Also, it is important to compare the performance of training on other datasets in MathInstruct, such as MATH dataset.

### Questions
1. GSM8K has about 7k training data, how do you get 14k examples?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper describes MathInstruct, a mathematical reasoning-focused instruction tuning dataset assembled from 13 constituent datasets, 6 of which the authors supplement with curated synthetic rationales from GPT4. The authors use MathInstruct to train MAmmoTH, a series of Llama-based fine-tuned language models for general math reasoning. The MathInstruct dataset contains a balance of Chain-of-Thought and Program-of-Thought rationales, allowing MAmmoTH models to predict intermediate outputs in either format. The authors exploit this ability by defaulting to Program-of-Thought prediction, then backing off to CoT prompting in the event a predicted PoT program fails to execute.

The authors conduct a comprehensive evaluation of a number of open-source language models on multiple datasets, both in-domain (held out splits of datasets appearing in their MathInstruct corpus) and out-of-domain. The proposed MAmmoTH models outperform the vast majority of open LLMs, and even manage to outperform most closed LLMs (aside from GPT4) on the MATH and AQuA datasets.

### Strengths
- Including both CoT and PoT intermediate reasoning in MathInstruct is a great move, as the strengths and weaknesses of the two techniques are largely complementary; the hybrid inference strategy exploiting both modes is both intuitive and effective, which is very satisfying.
- Focusing on the diversity of the corpus seems to have paid off, as Table 5 shows that MathInstruct fine-tuning outperforms the sum of its largest parts on the more challenging out-of-domain test sets like the SAT questions.
- It's always nice to see performance gaps between proprietary and open models closing.

### Weaknesses
 - It would be useful to have numbers for some of the closed models (that have APIs) for NumGlue, Mathematics, SimulEq and MMLU-Math. I realize this is a slightly annoying request as it incurs monetary costs and the scientific value of comparing to systems with unknown training distributions and architectures is dubious, but knowing which of these datasets are the most challenging for widely-used "flagship" models still has value as a heuristic for contextualizing the contribution.
- The authors only experiment with one approach to hybrid prompting - it seems like a number of approaches could be viable, e.g. self-consistency across samples from both CoT+PoT, or letting the model pick which mode to operate in. If other approaches were tried but weren't effective, it would be good to see results (or at least a remark) indicating what was tried and justifying the chosen approach as the best one empirically.

### Questions
1) You mention that PoT is "activated" by using a particular prompt trigger. Does this mean the model won't generate PoT rationales without specifying this trigger, or will it generate a mix of both by default? (Insight on this question could address part of my second bullet in the Weaknesses section)
2) Connected to the question above, it would be nice to add an overall ratio of PoT/CoT to Table 1. Summing and dividing the listed sizes gives 27% PoT, which explain the need for the PoT trigger prompt, but I couldn't find this number in the paper - did I miss it somewhere?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a newly curated instruction-tunning dataset for tunning open-source models for general math problems. The MathInstruct dataset contains 13 datasets and intermediate steps to arrive at the solution. They explored a hybrid of CoT and PoT rationales. As a result, the open-source models tunned by MathInstruct beat the current best open-source models finetuned for math problems as well as GPT-4 on a portion of the math datasets.

### Strengths
1. The paper demonstrated that hybrid rationales sourced from both Chain-of-Thought reasoning steps and Program-of-Thought coding capability achieved better performance than using just CoT or just PoT for math problems. 
2. Comprehensive results that compare models that are 1. differently sized and 2. differently instruction-tuned. This can be a very useful resource for anyone interested in studying the math reasoning capabilities of LLMs.
3. OOD scenarios are also considered and shown.

### Weaknesses
1. It is known that doing SFT on the dataset, especially with intermediate reasoning can do better. So even though MathInsutruct is already better than its competitors at generalizing, it can still remain a problem for even harder or unseen math problems.

### Questions
1. Is there a baseline that just finetunes all of the 13 datasets into 1 model? I think this would give a better idea of how to access MathInstruct. If not that's fine.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents MAmmoTH, a set of publicly available large language models specifically created for solving a wide range of mathematical problems. These models undergo training using a meticulously assembled dataset called MathInstruct, which is compiled from 13 different math datasets and includes detailed intermediate reasoning steps. MathInstruct is unique in that it incorporates a combination of two reasoning methods, chain-of-thought (CoT) and program-of-thought (PoT), spanning diverse mathematical domains. The use of both CoT and PoT enables these models to employ distinct problem-solving approaches for different types of math challenges. This study underscores the importance of embracing diverse problem types and employing hybrid reasoning techniques to enhance the development of highly capable mathematical generalist models.

### Strengths
This paper provides a very simple method to synthesize useful annotations to equip small LLMs with maths reasoning ability. The authors also conduct fairly comprehensive comparison against many existing maths models with a wide range of model sizes, regardless of in-domain/out-of-domain tasks. The ablation studies help us to better understand the influence of the subparts in the training annotations.

### Weaknesses
Despite the commendable performance exhibited by MAmmoTH, several notable weaknesses should be acknowledged:

**Limited Technical Novelty**: The approach employed in developing MAmmoTH bears resemblance to previous works, such as Orca (Mukherjee et al., 2023). In situations where an adequate reservoir of mathematical Chain-of-Thought (CoT) or Program-of-Thought (PoT) data is unavailable, the model resorts to generating content from scratch. While this approach serves as a valuable resource and addresses the scarcity of specialized mathematics models, it may not be considered a groundbreaking contribution without a more rigorous evaluation and innovative techniques.

**Absence of an In-Depth Analysis of Training Data Distribution**: It is evident that each dataset contributes unevenly to the final training annotations. For instance, TheoremQA contains a mere 600 samples, raising questions about the true impact of incorporating such a small dataset. While it is reasonable to assume an enhancement in TheoremQA performance, it remains unclear whether this addition adversely affects the performance of other in-domain and out-of-domain tasks. Additionally, there is a concern that the model's focus on other mathematics datasets may hinder its proficiency in learning TheoremQA.

**Insufficient Ablation Studies on Training Dataset Influence**: The majority of ablation studies appear to be centered around GSM8K, with the authors incrementally augmenting the training data size atop GSM8K. However, there is a notable absence of alternative strategies, such as initially training the model on MATH and subsequently introducing other datasets in a stepwise manner. Another informative ablation study could involve the removal of individual training datasets, such as M + C + A + N, and G + M + C + N, to elucidate the specific impact of each dataset on model performance.

**Lack of Comprehensive Error Analysis**: While MAmmoTH has demonstrated impressive performance, a detailed error analysis would provide valuable insights into areas where the model can further improve. The inclusion of illustrative examples could enhance our understanding of the model's strengths and limitations, aiding in the refinement of its capabilities.

### Questions
1. How much of the training data would be filtered after the validation? It would be good to know the data utilization rate for the data generation process.

2. I'm curious about whether the generated annotation converted from TheoremQA can be successfully executed, because the problems there would require many advanced calculation like integral and derivative computation.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes MMmmoTH, which consists of two main contributions. First, it combines many different math datasets together, to the MathInstruct dataset with 260k data samples. Secondly, it uses GPT-4 to geenerate hybrid CoT and PoT solutions for the problems in the dataset. After fine tuning Llama with math instruct, their method can achieve much better results compared with the existing methods.

### Strengths
I think the main strength of this paper is it provides better results on many math datasets, including GSM8K and Math.

Originality: the main originality of this paper is combining multiple math dataset together, and use hybird CoT and PoT as the solution for the problems in the dataset. However, the use of CoT and PoT is a common idea used in many math papers.

Quality: Good. This paper provides a clear pipeline of the algorithm, with detailed comparison with other methods.

Clarity: Good, it is easy to follow.

Significance: Mild, as stated below.

### Weaknesses
This paper has limited novelty, because it seems that it mainly combines all the math datasets together, and use GPT-4 to label the dataset, and then fine tune Llama with the new labels. This is a fairly standard pipeline, and it seems that the main improvement comes from the intelligence of GPT-4. 

Moreover, the idea of hybird instruction tuning is a bit confusing. According to Sec 2.4, the authors will first run PoT, and if the program cannot execute, they will switch to CoT. It seems to be a very preliminary way to combing CoT and PoT together. I was thinking a better way could be interleaving CoT and PoT in the solution. 

The fine tuning part of LLama is kind of straightforward, and there are many existing work using similar ideas. So I will not say it is an important contribution.

Overall speaking, I think the main contribution of this paper is "using GPT-4 to create a new dataset (which is a combination of many existing datasets), and fine tune Llama using the created dataset". Therefore, I will say this paper has limited significance. I give weak accept mainly because I feel this is an important problem, and the authors provide a reasonably good solution.

### Questions
I think the authors did not provide enough details about how CoT and PoT are mixed together. It seems that both CoT and PoT are simply treated as natural languages, and feed into the model for fine tuning? Are there any special tokens used? It seems that you only used "let's write a program to solve the problem" as the prompt, right?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

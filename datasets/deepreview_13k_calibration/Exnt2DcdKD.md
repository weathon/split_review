# NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 8, 6, 5, 5

## Abstract
We present Nirantar based on a large-scale effort to collect extempore and conversational speech data from participants spanning 22 languages across diverse locations in India. Given the extensive number of languages and locations involved, data is collected in incremental batches. Each batch introduces new languages, new domains (locations), or both, creating a practical playground for continual learning (CL). Nirantar contains a total of  3250 hours of human-transcribed speech data covering 208 Indian districts across 22 languages, with 1720 hours newly released as a part of this work. The data inflow and resulting multilingual multi-domain episodes are based on real-world data collection rather than simulated episodes commonly found in existing CL datasets. In particular, the amount of data collected and the number of languages and domains involved are not uniform across episodes, reflecting a practical and real-world continual learning scenario. This dataset serves as a playground for training and evaluating CL approaches in three different scenarios: Language-Incremental (LIL), Domain-Incremental (DIL), and the novel Language-Incremental Domain-Incremental Learning (LIDIL), which has not been studied before. To establish the dataset's usefulness, we evaluate several existing CL approaches within these scenarios. Our findings indicate that the behaviour of these algorithms varies across the three scenarios, emphasizing the need for detailed independent studies of each.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Nirantar is a large-scale dataset featuring 3,250 hours of human-transcribed speech across 22 languages from 208 districts in India, with 1,720 hours newly released in this work. Collected in incremental batches introducing new languages and locations, Nirantar creates a real-world continual learning (CL) setting that supports training and evaluation in Language-Incremental (LIL), Domain-Incremental (DIL), and the novel Language-Incremental Domain-Incremental Learning (LIDIL) scenarios. Initial evaluations show that CL approaches behave differently across these scenarios, highlighting the dataset's utility for diverse CL research.

### Strengths
- The dataset encompasses a diverse range of languages across India.
- They offer three distinct continual learning settings: Language-Incremental (LIL), Domain-Incremental (DIL), and the novel Language-Incremental Domain-Incremental Learning (LIDIL).
- The paper is well-written and easy to follow, with a comprehensive analysis included.

### Weaknesses
 - The first two settings, Language-Incremental and Domain-Incremental, have been explored in previous studies, including CL-mARS, which covers various CL methods in multilingual contexts (https://arxiv.org/pdf/2310.16931), and works by Sadhu et al. (https://www.isca-archive.org/interspeech_2020/sadhu20_interspeech.pdf), Chang et al. (https://arxiv.org/abs/2104.01616), and Li et al. (https://arxiv.org/abs/2302.01496), which investigate incremental domain setups. In light of these prior studies, the contribution here feels mostly incremental in these areas.

- The dataset focuses exclusively on languages from India, which provides rich diversity, though it could be beneficial to include an analysis of language relationships and similarities to understand their potential impact on performance. Expanding the dataset with additional languages from public datasets like FLEURS or CommonVoice, especially those with minimal similarity, would further strengthen the study.

- Additionally, task order is determined randomly, yet exploring the effects of task ordering on performance or providing an analysis that considers language similarity, task order, and performance metrics could add valuable insights.

- Finally, while the study examines rehearsal-based and regularization-based CL methods, incorporating architecture-based approaches, such as Progressive Neural Networks (PNN), Piggyback (PB), and Learning to Prompt (L2P), could offer a more comprehensive view, as highlighted in prior literature.

### Questions
Refer to weakness

### Soundness
3

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
4

### Summary
The paper introduces Nirantar, a new benchmark for continual learning (CL) in automatic speech recognition (ASR) that deals with real-world challenges of adding new languages and domains over time. Nirantar is based on a large dataset of 3,250 hours of speech across 22 Indian languages and 208 districts (domains), collected in phases that mimic real-world, incremental data collection.

The main contributions of the paper are:

1) New Data: The paper relies on existing dataset, but contributes an additional 1720 hours of newly collected speech data. 

2) Real Scenarios: the benchmark provides realistic settings for continual learning, including Language-Incremental Learning (LIL), Domain-Incremental Learning (DIL), and a novel Language-Incremental Domain-Incremental Learning (LIDIL), explored in ASR for the first time.

3) Comprehensive Benchmarking: The paper evaluates several popular CL methods (e.g., Experience Replay, Elastic Weight Consolidation) across all scenarios, offering a thorough comparison of CL approaches.

4) Open-Source Contributions: All resources from this work will be made publicly available to encourage further research in multilingual and multi-domain continual learning for ASR.

In summary, Nirantar provides a valuable benchmark that reflects real-world data collection and introduces new challenges for continual learning in speech recognition.

### Strengths
- **Novel Contribution:** The work is original, not only contributing newly collected data, but including a novel Continual Scenario for ASR: Language-Incremental Domain-Incremental Learning (LIDIL). This scenario provides a more realistic view of real-world multilingual and multi-domain environments compared to many CL datasets that rely on synthetic or structured data, making its impact relevant beyond the specific languages covered.
Comprehensive Evaluation: The evaluation is extensive, covering popular continual learning methods like Experience Replay, Elastic Weight Consolidation, and Memory-Aware Synapse, along with meaningful metrics. The benchmark also evaluates CL methods across three distinct scenarios (LIL, DIL, and LIDIL), offering a detailed and multi-faceted analysis that allows for a nuanced understanding of model behavior in varying incremental learning conditions.

- **Clarity and Structure:** The paper is structured logically, with clear definitions and explanations of the continual learning scenarios and metrics. The description of data collection, experimental setups, and training procedures is transparent, with steps and design choices explained in detail. This clarity makes it easier for researchers to replicate or build upon the work.

- **High Impact for Low-Resource ASR:** The benchmark is valuable for advancing low-resource ASR research, especially for underrepresented languages like Indian languages. By focusing on multilingual, multi-domain continual learning, the benchmark tackles unique challenges in low-resource ASR.

- **Open Access:** the open release of the dataset and resources under a permissive license further promotes research and collaboration in the field, supporting wider accessibility of multilingual ASR technology.

### Weaknesses
 - **Limited Baselines:** While the paper evaluates CL methods from replay-based and regularization-based approaches, it excludes architecture-based methods arguing they are impractical for real-world settings as they add parameters for each new language and domain, leading to excessive complexity as episodes increase (lines 328-332). However, this overlooks recent advances in lightweight architecture-based methods like language-specific adapters, which have improved ASR performance even in domains harder than the training data [1]. Specifically, the exclusion of adapter-based methods limits the exploration of parameter-efficient techniques that could offer a better trade-off between adaptability and model size. For instance, adapters integrated within transformer layers could provide a more nuanced approach to handling new languages and domains without drastically increasing the model's parameter count. Including such methods could provide valuable baselines and insights into scalable alternatives that balance parameter efficiency and adaptability. Furthermore, the paper does not explore other efficient architectural modifications, such as low-rank adaptation or conditional computation, which could be relevant for continual learning in resource-constrained scenarios.

- **Discussions on Cross-Lingual Transfer:** The dataset is highly diverse, covering 22 Indian languages and 208 districts, but this diversity is underexplored in the analysis. A more granular breakdown of metrics would allow a clearer view of knowledge transferability across closely related languages and domains. For instance, including subgroup analyses by geographic distance, language family, or dialectal variations could highlight the impact of linguistic and regional proximity on model performance. Such details would enhance understanding of the effectiveness of CL techniques in low-resource settings. For example, on line 465, the authors attribute a performance decline to the introduction of a Tibeto-Burman language into the dataset predominantly composed of Indo-Aryan and Dravidian languages. Expanding on this, with metrics grouped by language family or linguistic characteristics, would provide more actionable insights into cross-language transfer. Additionally, including dataset attributes like vocabulary overlap, phonetic variations, or language family classification would better showcase the dataset’s uniqueness and clarify the transferability of findings to other low-resource multilingual datasets. The analysis should also consider the impact of varying degrees of linguistic similarity on the effectiveness of different CL methods, as some methods might be more suitable for transferring knowledge between closely related languages, while others might be better for more distant ones.

### Questions
1) Could you provide details on how human subjects were compensated and whether explicit consent was obtained for both research and potential industrial use of their voices? Including protocols and consent guidelines in the appendix would be helpful.

2) I recommend providing sample data in the appendix to illustrate the dataset.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Nirantar, a dataset designed to facilitate continual learning (CL) through real-world, large-scale speech data from 22 Indian languages. Data is gathered incrementally across diverse languages and domains, making it distinct from typical CL datasets that rely on simulated episodes. 

Nirantar support 3 key CL scenarios: Language-Incremental (LIL), Domain-Incremental (DIL), and the novel Language-Incremental Domain-Incremental Learning (LIDIL), which has not previously been studied. The authors’ evaluation of several existing CL algorithms in these scenarios reveals that algorithmic behavior varies significantly across them, suggesting the need for dedicated analyses tailored to each scenario.

### Strengths
The dataset’s design closely mirrors real-world CL requirements, providing a valuable resource for research on multilingual, multi-domain, and incremental learning.

The inclusion of both widely used CL scenarios (LIL, DIL) and the novel LIDIL scenario represents a significant contribution, opening new avenues for research.

Evaluations of CL approaches provide useful initial insights, underscoring the complexity and variability of performance across the dataset’s scenarios.

### Weaknesses
Figures 3-5 in the report show fluctuating trends, which might indicate an imbalance in the amount of data available for each language. This imbalance could impact the model's performance on specific low-resource languages, potentially limiting its effectiveness in some areas.

While the evaluations provide a starting point, a deeper exploration of algorithmic adaptations or optimizations specifically for LIDIL could enhance the study’s practical impact.

### Questions
Given the natural variations in data size per language and domain, what strategies are recommended to handle data imbalance in the CL models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Nirantar, a dataset designed for studying continual learning methods.
The dataset comprises batches of data for various Indian languages and Indian districts.
Various continual learning methods are analyzed on the language incremental, domain incremental and language incremental domain incremental setups.

### Strengths
* Continual learning is an important (as it relates to data efficient learning) and unsolved problem.
* The dataset seems valuable for studying continual learning and also beyond that as it supplements existing multilingual ASR corpora with mid/high/low resource data from Indian languages.
* Experimentation is reasonably thorough and tests different CL methods in various setups.

### Weaknesses
 * It's unclear whether the design of the dataset makes it unique to test CL methods. For example, a similar scheme could be adopted by taking the various releases over time from Common Voice (the domains would not be obtained in a straightforward manner though). The paper does not really demonstrate that the dataset provides value over  taking an existing dataset and slicing it into episodes.
* Related to the previous point, if the methodology to collect the data is the same as for IndicVoices, the contribution for this paper becomes less clear (other than adding more volume).
* A more minor weakness: the writing could be improved, for example by justifying all empirical choices (see clarification questions)



### Questions
* 269: “we select the 11 languages having the largest number of hours in Table 1”. Why is the largest number of hours chosen?
* 309: “We create timelines of length τ = 11”. Why was 11 chosen?
* 377: “Average MER: Match Error Rate”. Why not use WER or CER?

presentation: the citation formatting is unusual and can be double checked/fixed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduce Nirantar, a large-scale dataset designed for continual learning (CL) in ASR, spanning 22 Indian languages and over 3,250 hours of human-transcribed speech. This dataset includes diverse domains, represented by 208 districts across India, to model real-world multilingual, multidomain CL challenges.

Nirantar's primary contributions include establishing 3 CL scenarios—Language-Incremental Learning (LIL), Domain-Incremental Learning (DIL), and Language-Incremental Domain-Incremental Learning (LIDIL). The LIDIL scenario is novel, introducing both new languages and domains across episodes, a setup that reflects real-world data inflow patterns and has not been previously explored in CL.

To validate the dataset's utility, the authors benchmark several existing CL techniques (including Elastic Weight Consolidation, Experience Replay, and Memory-Aware Synapse) across the 3 scenarios. Experiment results suggest potential areas for improvement in CL approaches for multilingual, multidomain ASR.

### Strengths
### Originality
The Nirantar dataset presents a valuable resource for the speech research communities. With 22 Indian languages and over 3,250 hours of human speech, including 1,720 hours newly released as part of this work, and human-annotated transcriptions, the dataset spans a wide variety of topics, domains, and conversational scenarios. The paper introduces a novel Language-Incremental Domain-Incremental Learning (LIDIL) scenario, expanding beyond the traditional Language-Incremental (LIL) and Domain-Incremental (DIL) scenarios that form the three core scenarios of the Nirantar dataset. The inclusion of LIDIL sets a new benchmark for future studies in multilingual and multidomain CL under real-world scenarios.

### Quality
The paper is structured-well and offer a clear overview of the data collection, scenarios, and experimental evaluations on existing CL approaches.

### Clarity
The authors present a clear breakdown of 3 CL scenarios.

### Significance
The dataset’s breadth across 22 Indian languages and 208 districts makes it a valuable resource for developing speech models adaptable to language and domain shifts.

### Weaknesses
The paper does not report pre-CL performance metrics, such as Word Error Rate (WER,) for individual episodes across languages and domains, which limits understanding of Nirantar’s distinctiveness as a CL dataset. Specifically, existing ASR datasets like GigaSpeech 2 could be reorganized to create a comparable multi-domain, multilingual LIDIL dataset, so to strengthen its case as a novel CL dataset, additional evidence is needed. For instance, including initial statistics per language, domain, and episode would provide insights into each batch's difficulty across diverse linguistic and regional characteristics, highlighting its uniqueness as a new ASR CL dataset. Additionally, including initial ASR WER would help clarify Nirantar's quality as an ASR dataset.

### Questions
### Dataset Quality: 
1. Could you provide details on the quality assurance procedures and any pre-CL performance metrics, such as initial Word Error Rate (WER), to validate transcription accuracy across languages/domains/episodes? Understanding these methods and statistics would clarify the dataset’s reliability and distinctiveness for continual learning applications.

2. Could you elaborate on the procedures to ensure topic and domain diversity across districts, and how this diversity is measured or validated in different episodes? These insights would help demonstrate the dataset’s capacity to represent unique linguistic and regional characteristics, supporting its role as a comprehensive ASR CL dataset.

### Soundness
2

### Presentation
2

### Contribution
3

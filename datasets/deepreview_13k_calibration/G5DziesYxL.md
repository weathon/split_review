# Bridging the Data Provenance Gap Across Text, Speech, and Video

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 5, 8, 8

## Abstract
Progress in AI is driven largely by the scale and quality of training data. Despite this, there is a deficit of empirical analysis examining the attributes of well-established datasets beyond text. In this work we conduct the largest and first-of-its-kind longitudinal audit across modalities---popular text, speech, and video datasets---from their detailed sourcing trends and use restrictions to their geographical and linguistic representation. Our manual analysis covers nearly 4000 public datasets between 1990-2024, spanning 608 languages, 798 sources, 659 organizations, and 67 countries. We find that multimodal machine learning applications have overwhelmingly turned to web-crawled and social media platforms, such as YouTube, for their training sets, eclipsing all other sources since 2019. Secondly, tracing the chain of dataset derivations we find that while less than 33% of datasets are restrictively licensed, over 99%, 78%, and 99% of the source content in widely-used text, speech, and video datasets, respectively, carry non-commercial restrictions. Finally, counter to increasing absolute multilingual and geographic inclusion in publicly available AI training data, our audit demonstrates measures of relative geographical and multilingual representation have failed to significantly improve their coverage since 2013. We believe the breadth of our audit enables us to empirically examine trends in data sourcing, restrictions, and Western-centricity at an ecosystem-level, and that visibility into these questions are essential to progress in responsible AI. As a contribution to ongoing improvements in dataset transparency and responsible use, we release our entire multimodal audit, allowing practitioners to trace data provenance across text, speech, and video.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper conducts a large-scale dataset audit across text, speech, and video modalities, covering near 4000 public datasets between 1990-2024 by investigating their sources, use restrictions, and their geographical & linguistic representation. It is found that 1) Many multimodal ML datasets are from web-crawled and social media platforms; 2) Inconsistencies between dataset licenses and their source's restrictions prevail; and 3) Inequality in geographical representation remains very high, and geographical & linguistic representation has not significantly improved for many years.

### Strengths
• The paper is well-motivated: Most previous works has primarily focused on text datasets, or a single feature or dataset. The paper conducted a multimodal and multi-feature dataset, which addresses this gap.

• The scale of this study is impressive: It covers nearly 4000 datasets, 3 modalities (text, speech, video) and a time span of over 30 years (1990~2024), providing a comprehensive view to dataset provenance study.

• The study points out vulnerabilities of current dataset sources. For example, the paper discovers prevailing inconsistencies between dataset licenses and their source's restrictions, alarming the research community about potential legal breaches. The paper also reveals that many measures to address geographical & linguistic fairness have failed, surprisingly, which motivates the research community to retrospect these measures and potentially propose new (effective) ones.

### Weaknesses
• The paper mentions a rise in synthetic data, but does not give any in-depth analysis of synthetic data v.s. non-synthetic data. I think it is worthwhile to analyze the source distribution of synthetic data v.s. non-synthetic data, so that researchers can know the search space where they are more likely to acquire desired data when they need human-written or machine-generated data. Specifically, the paper should investigate the proportion of synthetic data across different modalities (text, speech, video) and how this proportion has changed over time. Furthermore, it would be beneficial to analyze the specific methods used to generate synthetic data (e.g., GANs, text-to-speech, video synthesis) and how these methods impact the characteristics of the resulting datasets. This analysis could reveal potential biases or limitations introduced by synthetic data generation techniques.

• The paper is not technically savvy, so it is crucial for the paper to highlight the importance of its insights. Given the large-scale of this study (nearly 4000 datasets) and the engagement of domain experts for annotation tasks, the study should be costly. But the paper did not make it very clear that why studying data provenance (probably with such high cost) is valuable at the first place. Why not use the same annotation labors to create new dataset resources instead, but studying the provenance of existing dataset (intuitively, the former one can be more valuable)? The paper needs to articulate the unique value proposition of data provenance studies. It should emphasize how understanding the origins, licenses, and biases of existing datasets can prevent the propagation of errors and biases in downstream models, which could be more cost-effective than creating new datasets from scratch. The paper should also discuss how data provenance analysis can inform the development of more robust and reliable machine learning systems by identifying potential vulnerabilities in training data.

### Questions
• Given that the study includes datasets from 67 countries, when studying data licenses or terms of use, are difference in legal regulations of copyrights between countries/regions taken into consideration?

### Soundness
2

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
4

### Summary
In this paper, the authors present an audit of nearly 4000 public datasets between 1990-2024, spanning 608 languages, 798 sources, 659 organizations, and 67 countries. They further present their analysis of data sources, geographical and multilingual inclusion.

### Strengths
The paper is well written and easy to understand. The authors explore an important topic relevant to extremely fast-paced growth of AI models and their adoption. They explore a large-scale collection of datasets across three modalities: text, speech and video. They further present interesting analysis highlighting the community inclusion for dataset creation and the restriction on the usage of the datasets. The study brings out the inequality in geographical representation and the multilingual representation and furthermore the situation has not improved significantly over the last decade on most measures.

### Weaknesses
I find the lack of call-to-action from the authors. There are no concreate directions presented in the paper that could help improve the situation. A mere analysis of the landscape is probably not going to be of much help given the pace with which the field is evolving. They have surveyed so many papers which should have nudged them to form an opinion on the next course of action for the community. 

Also, since this field is growing rapidly, the analysis presented here would become obsolete very quickly. What might help in the long-term is to build a tool that can automate the analysis presented here with such dedicated effort.

### Questions
See my comments in the weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work conducts a large-scale and comprehensive audit of nearly 4,000 text, speech, and video datasets between 1990-2024, covering a wide range of tasks, languages, sources, organizations, and countries. Specifically, the authors analyze data trends for the state of data permissions (licenses and terms), sourcing (the web, human annotation, and synthetic generation), and representation (of tasks, organizations, languages, and countries). The datasets included in the audit include those that are publicly available, widely used for general-purpose model development, and relevant to generative tasks. Overall, the authors analyzed 3.7k text, 95 speech, and 104 video datasets. 

The analysis revealed an increasing use of data from web-crawled, social media, and synthetic sources, driven by scaling laws. This was particularly prevalent in speech and video datasets, with YouTube being the most prominent source. The contribution of synthetic text data has also rapidly become significant in recent years. Additionally, the authors found inconsistencies in data source terms and documented license restrictions, with the former being much more restrictive. Further, many data collections do not clarify commercially licensed versus restrictive datasets. Finally, the analysis revealed that while there has been an increase in the languages and countries represented in the datasets, the relative contribution remains Western-centric.

### Strengths
* The paper provides novel insights from a large-scale and comprehensive audit of widely used datasets across text, speech, and video modalities.
* The paper is well-written and organized.
* Larger implications of the authors’ findings are discussed, highlighting challenges and suggestions for practitioners.

### Weaknesses
 * The audit does not include image datasets, which are widely used in multimodal settings.
* The analysis does not include the tasks that the datasets are designed for.
* Some more insights and analysis can be provided for the cause of observed trends- e.g. the sharp rise in encyclopedia-based and internet video-based sources in text and speech datasets after 2018, the drop in the Gini coefficient for geographic representation in video datasets after 2019, etc.

### Questions
* Can the source of synthetic datasets (e.g. the models they were generated from) be determined? Are there any challenges in determining such sources?
* Why was the scope of the datasets limited to generative tasks?
* Was there a variation in the tasks represented by the data across the years? It would be interesting to observe emerging trends in AI research over the years (e.g. code generation and other domain-specific tasks).
* Was the correlation between data sources and language/geographical diversity analyzed?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors conduct a comprehensive audit across modalities—popular text, speech, and video datasets—from their detailed sourcing trends and use restrictions to their geographical and linguistic representation.

### Strengths
1. This is an extremely exciting work for multi-modal researchers, as one of the main bottlenecks is how to get balanced and good quality data from the wild. This work deepens the communities understanding of multi-modal data conditions at present and in the history.
2. The authors conducted rigorous data collection and analysis work, which deserves much credit.
3. The insights provided are valuable and interesting, which may provide great inspirations for people curating multi-modal data from real world.

### Weaknesses
1. I feel the data collection specifications are limited. Though the authors has mentioned that the discussion for geographical and linguistic representation is limited, I think more discussion should be casted on the data collection methods, as this is the foundation of all discussions in this work. How to ensure the recall and precision of data collection? The data and its conclusion could easily get biased when missing or mistakenly putting a large dataset into the data pool.

### Questions
1. I'm curious that did you perform analysis on the portion of synthetic data and their characteristics? I think this is one of the most concerned topics by far, though it's really hard to correctly collect all the data.

### Soundness
3

### Presentation
3

### Contribution
3

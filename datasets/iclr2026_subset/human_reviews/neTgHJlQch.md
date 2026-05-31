## Human Reviewer 1

### Summary
Benchmarks often measure factual knowledge of LLMs in high resource languages or regions or related to high frequency entities.  The paper proposes a method called CHOLCO for evaluating the knowledge of LLMs across entities related to traditions, public figures, food and geography. The paper uses Wikidata to extract triples across three regions: Latin America, Europe and United States and converts it into a question. They evaluate LLMs on these questions along with a probe based evaluation technique to understand what the LLM knows about these rare entities.

### Strengths
1. The paper provides a scalable approach to building a benchmark for less known entities across different regional contexts by using Wikidata to source triples and converting them to templated questions. It provides a comparison of different models' performance across the three regions: United States, Europe and Latin America. 

2. The paper compares the performance of different models on factual information across regions and highlights that models perform worse on information related to Latin America.

### Weaknesses
1. There is no clear basis for the evaluation technique used in Sec 3.2.1 where the authors compute the LLM performance on their benchmark questions based on embedding similarity, lexical overlap, LLM as a judge and multiple choice accuracy. Using LLM as a judge would suffice in this scenario and it is not clear what value the other methods add. Methods such as lexical overlap are potentially noisy as LLMs tend to be verbose and the expected answer is usually a single location. 

2. Sec 3.1 talks about the properties used for building the dataset: "country of origin (property P495), country of citizenship (P27), place of birth (P19), territorial location (P131), and geographic coordinates (P625)." This seems to be a very limited set of properties which would always cause the label to be a location. This limits the diversity of the answers in the benchmark. 


Presentation: 
1. In Table 2, QWEN should be replaced with the entire model name.

### Questions
1. For the evaluation setup, the authors evaluate GPT 3.5 Turbo and GPT-5 Mini, but not GPT-4 or GPT4o. Is there any specific reason for this?

### Soundness
1

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper analyzes regional knowledge of Latin America in LLMs. Specifically, this paper first extracts structured facts from domain-specific resources and constructs a knowledge graph containing 44,000 entities spanning 9 categories. Using this knowledge resource, this paper proposes CHOCLO, an entity-centric methodology for evaluating LLM knowledge of culturally relevant entities in Latin America. It evaluates the regional knowledge in LLMs using several techniques, including token overlap, embedding similarity, LLM-as-a-judge, and multiple-choice accuracy. This paper also trains a probing model to evaluate the factual score directly from LLM representations. This paper finds several interesting conclusions, such as most LLMs underperform in  Latin American knowledge.

### Strengths
1. The topic is interesting and meaningful to the community. Studying LLMs’ coverage of different regional knowledge is important for the broad applications of LLMs.
2. The work presents a systematic analysis and comprehensive experiments. The experimental results reveal that current LLMs underperform on Latin American knowledge. This provides some guidance and insights for improving LLM knowledge coverage and supports the development of more diverse LLMs and broader applications for people all over the world.

### Weaknesses
1. The authors construct a knowledge graph, but there are existing resources (e.g., Wikidata). The paper should analyze whether the constructed knowledge graph adequately captures Latin American knowledge. And what is the advantage compared to existing resources? Is this knowledge graph covering more Latin American knowledge?
2. The methods used for experimental analysis are mostly existing techniques, which limits the paper’s technical novelty.
3. The authors should evaluate the reliability of their evaluation approaches. For example, they can analyze the correlation between each evaluation method and human judgments, to validate the reliability of their evaluation methods.
4. A more fine-grained analysis specific characteristics of Latin American knowledge is needed. The authors should discuss how Latin American knowledge differs from other regional knowledge and why LLMs underperform, such as insufficient training data or other factors, to guide further LLM development.

### Questions
See Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper introduces CHOCLO, a framework to evaluate regional and culturally grounded knowledge about underrepresented regions in Large Language Models (LLMs). To do so, the authors curated a dataset with ~44k entities and ~130k questions, spanning across different categories adapted from CVQA: dish, flora, fauna, geography, object, public figure, tradition; ensuring broad thematic coverage while capturing cultural patterns. The authors argue that existing mainstream datasets are skewed, hence LLMs lack cultural knowledge, and therefore focus the analysis on the coverage of entities related to Latin America. CHOCLO uses structured knowledge graphs (KGs) to evaluate factual knowledge at the entity level via four complementary scoring methods, followed by a probing model to predict factual knowledge scores. Experiments show that GPT-3.5, GPT-5, Mistral, DeepSeek, and Qwen demonstrate performance disparities specifically with entities related to LATAM compared to the USA and Europe.

### Strengths
1. The paper tackles an important aspect of LLMs - information inclusivity. 
2. The evaluation pipeline, containing structured KG-based QA and probing with 4 scoring methods, offers different aspects of understanding of factuality. 
3. The paper presents a detailed quantitative analysis at - cross-region and category level. The results confirm the disparities in information content in LLMs.

### Weaknesses
1. The dataset curated for this evaluation relies entirely on Wikidata as the primary source of information. However, there is inherent coverage bias in Wikidata on region-specific knowledge. No analysis has been provided on that.
2. The proposed framework is not technically novel. It combines a couple of existing, well-established methods to evaluate the region-specific LLM knowledge. Moreover, the semantic meaning of the predicted scores is not clear. It is missing statistical significance tests or NLI tests for a better understanding of predicted scores. 
3. The paper emphasises cultural knowledge inclusion in the LLMs, but considers LATAM as a homogenous region, hence also increasing the risk of over generalisation based on languages/linguistic features. The work would have benefited from some analysis based on that.
4. It would be nice to have the framework tested out for CultureBench

### Questions
1. What is the impact of Wikidata coverage bias on your framework, and how to deal with it? 
2. How do you ensure the quality of the extracted triple? 
3. How do you find the agreement between the different scoring functions?
4. Could the probing scores increase biases instead of mitigating?
5. How do you avoid the overgeneralisation of the analysis done based on the assumption that LATAM is a homogeneous region?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3
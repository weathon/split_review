# NovoBench-100K: A large-scale protein dataset for in silico evolution of de novo TadA

- Decision: Reject
- Scores: 3, 6, 6, 3, 5

## Abstract
We introduce NOVOBENCH-100K, a large-scale protein dataset for the in silico evolution of TadA, an enzyme critical for base editing. This dataset originates from the sequencing data collected during two rounds of our in vitro TadA evolution, encompassing 101,687 unique DNA variants with an average of 11.1 amino acid mutations. Rather than employing classes or scores as labels, our dataset consists of 77,900 ranking lists, each involving 2, 10, or 100 sequences ranked by their base editing efficiency. These rankings are generated using our SEQ2RANK, a novel algorithm that accounts for biological experiment credibility and ranking consistency. For evaluation, we provide two train-test splits, designated as in-domain ranking and out-of-domain ranking, based on a standard 7:3 random split and the actual in-vitro evolution rounds, respectively. We benchmark 80 biological language models (BLMs) across 24 papers, spanning protein, DNA, RNA, and multimodal domains. Comprehensive experiments reveal that BLMs perform well on in-domain ranking, with a detailed analysis by modality, model size, and K-mer. However, for out-of-domain ranking, BLMs exhibit poor performance in both linear probing and fine-tuning, resembling random guessing. This underscores the necessity for highly generalizable models to address domain shifts between experimental rounds. Finally, our wet experiments are ongoing to generate more data to expand our benchmark. In a few months, we expect to add additional rounds of in vitro evolution and include a broader variety of proteins. We will release the code, dataset, and embeddings of our evaluated 80 BLMs soon.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces NOVOBENCH-100k, a very large-scale benchmark dataset for a base editing enzyme TadA derived from in vitro evolution experiments in wet lab. The experimental data covers 100k DNA variants with an average of 11.1 amino acid mutations, exceeding existing datasets for protein function prediction. The authors generated multiple ranking lists of sequences as opposed to reporting absolute read count as labels, and proposed an algorithms SEQ2RANK that creates partial ranking lists of sequences with the aim to improve ranking consistency at experiment-level and sequence-level. They benchmarked 80 biological language models spanning different sequence modalities on both in-distribution and out-of-distribution train-test splits, and showed preliminary results that BLM fails to predict well in out-of-distribution setting.

### Strengths
The paper introduced a new benchmark dataset for protein function prediction which excel at its scale and data quality. With 2 rounds of in-vitro evolution of TadA, the authors created a dataset with large amount of mutations and diversity. Such real-world wet-lab experiments data could be a valuable source of data for protein design community. The data is at DNA level and can be used for multiple biological sequence modalities including DNA, RNA and protein sequences. The introduction of ranking list as opposed to absolute value is not new, but the algorithm for list construction does take into consideration several realistic challenges.

The benchmarking effort is also very extensive, covering 80 BLMs and both in-distribution and out-of-distribution. The OOD setting with different evolution round is a novel setup.

### Weaknesses
The data could be valuable source for MLCB community, however since it is considering one specific protein TadA and base editing enzymatic activity, the generalizability could be limited. Moreover, the majority of the work focuses on data creation and benchmarking, the technical contribution and novelty may be insufficient for an ML venue. The idea of using ranking instead of absolute value is introduced in many prior work.

The key technical contribution, Seq2Rank algorithm, is introduced in 3.3, but the writing is too high-level and lacks rigorous definition and mathematical justification. Significant amount of details is put into appendix, Algogirhtm1, which is still too abstract and could not justify for the claim of an effective algorithm that address experimental sensitivity.  

According to algo1, it sorts list of experiments by reliability and go over the list of lists from high to low order. Within each list, it constructs dictionary of read counts and apply some greedy sampling strategy to sample “strict” partial ordered list that only contain single sequence for a given count, without introducing cyclic loops into the DAG constructed from data that are already been processed. The “GREEDY_SAMPLE” algorithm is too abbreviated and lacks details, such as how are the read count index sampled at each step, and with what “greedy” order it traverse the possible sequence space.

The proposed SEQ2RANK could also introduce biases. For example, strictly enforcing sampling one sequence at each bin breaks the original value distribution of the reads. It is also not clear whether the generated list can cover similar value range, or some of them will be biased towards higher region. When adding sequences from different experiments into same graph, it implicitly tries to compare read counts across different experiments, which may not be ideal. 

Additionally, the algorithm requires definition of reliability from biological priors. The later experiment is strictly more important regardless of the read count value, which may not be true all the time. What if such prior does not exist and there is naturally uncertainty in two replicated experiments that needs to be considered equally?

Figure 4 is not informative about Seq2rank and does not have good correspondence with algorithm 1 in appendix.

### Questions
1.	When talking about credibility, it mentions “later rounds are more reliable”. Is this suggesting that read counts across different rounds are compared? E.g., it might compare the read count of seq A in round 1 with the read count of seq B in round 2?
2.	What if there are experimental replicas that may have a batch effect but we don’t necessarily have a “reliability” measure of the replicas and want to consider them as equally important?
3.	If seq A has a very high value in round 1, but is somehow close to noise low value in round 2, given that round 2 is always given higher reliability seq A will be ranked low?  What if the round 2 data is noise, and such an assignment might create a lot of wrong ordering of sequences relative to seq A?
4.	How do we determine what read count index to use in each step of GREED_SAMPLE?

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
4

### Summary
This paper presents a large-scale dataset comprising approximately 100k DNA variants for in silico TadA evaluation, using this dataset to benchmark 80 BLMs. The data, collected from PANCE experiments, is organized into consistent ranking lists of varying lengths (2, 10, and 100) using a novel algorithm, SEQ2RANK. SEQ2RANK mitigates conflicts at the experiment level by prioritizing experiments based on credibility and ensures strict sequence-level consistency through a DAG. This dataset is used to assess model capability via ranking tasks and includes two train-test splits: in-domain and out-of-domain. The BLMs are tested through linear probing and fine-tuning. In the ranking task, where BLMs are used as encoders, model embeddings generally outperform one-hot embeddings. Experiments across modalities show that Chai1’s performance is consistent across different modalities, while LucaOne performs better on proteins than nucleotides. The performance of models of various sizes also demonstrates scaling laws across protein, DNA, and RNA modalities. However, the BLMs perform poorly on the out-of-domain split, highlighting limitations in their practical robustness.

### Strengths
1.	The paper conducts extensive experiments to evaluate the capabilities of BLMs on TadA. The authors tested a diverse set of 80 BLMs spanning 24 papers on the NOVOBENCH-100K dataset. These BLMs represent a range of modalities, including: protein, DNA, RNA, multimodal BLMs. The authors evaluated these BLMs using both linear probing and fine-tuning. Authors also tested three different learning rates (1e-5, 1e-4, and 1e-3) for each experiment and reported the best result. The evaluation across a wide range of BLMs, evaluation methods, and hyperparameters contributes to a comprehensive evaluation of BLMs on the TadA protein evolution task.
2.	The NOVOBENCH-100K dataset originates from two rounds of standardized PANCE experiments and includes 100k sequences, making it valuable for research in this domain. The authors also promise to include more rounds of wet experiment data. 
3.	The two rounds of experiments provide a useful approach for creating an out-of-domain train-test split. This split offer a practical perspective on model’s robustness in the real-world applications. 
4.	The dataset organizes sequences into ordered lists of varying lengths, rather than using scores or labels, to mitigate experimental noise and address scalability limitations. The authors propose SEQ2RANK, which incorporates the credibility of each experiment to ensure the consistency of the ranking data.
5.	The paper is clearly written and well structured. The presentation is pretty good.

### Weaknesses
1.	The experiments primarily use BLMs as encoders, leveraging the embeddings for downstream ranking tasks. However, there are other common approaches, such as prompting and in-context learning, which are now widely used. The authors should consider including these methods in the evaluation.
2.	There are additional aspects that could be included in the analysis, such as details about the model architectures (e.g., encoder-decoder or decoder-only). Additionally, providing more description of the initial design purpose of each model and how this aligns with the TadA evaluation would be helpful.
3.	It would be beneficial to conduct more rounds of experiments, as I am questioning whether the model's poor performance on out-of-domain cases is due to overfitting to a specific experimental round. I notice that the author plans to include additional rounds of wet experiment data, which I am looking forward to seeing.
4.	The authors should include detailed descriptions of the wet experiment conditions as a reference for researchers who wish to replicate or expand this dataset.

### Questions
1.	There is an existing benchmark names NOVOBENCH (without the 100k) (https://github.com/Westlake-OmicsAI/NovoBench). What is the relationship between NOVOBENCH and NOVOBENCH-100K?
2.	What are your insights on why all models fail in out-of-domain evaluation, and how can the models' robustness be improved for out-of-domain cases?
3.	Why do conflicts arise in the rankings? If these conflicts are due to experimental errors, should the algorithm identify and exclude erroneous experiments from the data, rather than simply using credibility to mitigate the conflicts?

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
This paper introduces NOVOBENCH-100K, a large-scale dataset aimed at advancing the in silico evolution of the TadA enzyme, a critical component in base editing. This dataset is unique as it provides 101,687 DNA variants and employs a novel ranking-based approach, SEQ2RANK, rather than traditional classification labels, to account for the biological experiment's credibility and ranking consistency. The authors also benchmark 80 biological language models (BLMs) across protein, DNA, RNA, and multimodal domains, demonstrating these models' proficiency in in-domain tasks while highlighting challenges in out-of-domain ranking.

### Strengths
Novel Dataset: The creation of NOVOBENCH-100K fills a crucial gap in protein engineering, specifically for base editing.
Robust Methodology: The SEQ2RANK algorithm ensures data consistency and robustness, addressing typical noise and variability in biological data.
Comprehensive Benchmarking: The inclusion of various BLMs and modalities provides a detailed performance landscape, especially in distinguishing in-domain from out-of-domain capabilities.

### Weaknesses
Limited Real-World Application Validation: Although the dataset is extensive, there is limited discussion on how it performs in real-world applications beyond the in silico setting. Including preliminary results from practical applications or collaborations with experimental labs could strengthen the paper. Specifically, the paper lacks concrete examples of how the dataset's ranking translates to actual protein activity improvements in a lab setting. The absence of validation using orthogonal experimental methods, such as in vitro assays, makes it difficult to assess the dataset's practical utility.
Out-of-Domain Generalization: The authors highlight the poor performance of current BLMs on out-of-domain rankings. However, the paper could benefit from a more in-depth analysis of why these models fail and potential strategies for overcoming these limitations. The paper does not explore the specific characteristics of the out-of-domain data that cause these failures, such as sequence divergence or novel structural motifs. A more detailed investigation into the types of errors made by the models could provide valuable insights.
Benchmarking Scope: Although 80 models are benchmarked, it would be beneficial to include additional model families or discuss other state-of-the-art models in more detail to contextualize their choices further. The current benchmark lacks a clear rationale for the selection of these 80 models, and it's unclear if the benchmark includes a diverse set of architectures, training paradigms, and pre-training datasets. A more detailed analysis of the model selection process would be beneficial.

### Questions
Can the authors clarify if SEQ2RANK can be generalized to other protein datasets or if it’s specifically tailored for the TadA evolution? This would help in understanding its broader applicability.
Are there plans to address the out-of-domain challenges identified in the paper, perhaps by incorporating domain adaptation techniques or more diverse training data?

### Soundness
4

### Presentation
3

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
This paper introduces a new dataset called NOVOBENCH-100K, which contains 101,687 unique DNA variants with an average of 11.1 amino acid mutations. This dataset can be used to evaluate biological language models (BLMs), including pLM, DNALM, and RNALM. The authors assessed 80 BLMs across both in-domain and out-of-domain scenarios. They have released some code and data.

### Strengths
(1) Provides a large-scale dataset that can be used for computer evaluation of various machine learning algorithms;
(2) Conducts an extensive study of 80 BLM models in both in-domain and out-of-domain ranking scenarios;
(3) The paper is well written;

### Weaknesses
There are several concerns regarding the evaluation presented in this paper:

**Dataset Division**: To rigorously evaluate a machine learning algorithm, it is necessary to prepare separate training, validation, and test sets. However, this work only partitions the dataset into training and test sets. It is not a good practice to use the test set to tune hyperparameters (e.g., batch size, early stopping, or training epochs). The test set here is actually a validation set. A good performance on the validation set does not mean that the results on the test set will be similar.

**Evaluation Method**: The paper primarily evaluates linear probing in the main text, but linear probing typically performs significantly worse than fine-tuning the entire model or the top several layers of the language model. I noticed in the appendix Table 6 that the authors only evaluated ESM2 using both linear probing and all-parameter fine-tuning, revealing a substantial performance gap (e.g., the SP metric increased from 0.138 to 0.208 and from 0.075 to 0.187). Given this difference of pLM, I suggest the authors present the main results for these pLM algorithms using parameter fine-tuning rather than a frozen embedding strategy. 

**Evaluation of Multiple Models**: The authors claim to have evaluated up to 80 biological language models (BLMs), which seems quite surprised to me. Each model's hyperparameters should be meticulously tuned. How can the authors ensure that they are using each model correctly or with optimal settings? If suboptimal settings were used, the benchmark may not be reliable. For instance, SaProt is a protein language model that incorporates structural information, yet the paper does not specify what type of structures were used (PDB or AlphaFold2 structures with or without pLDDT). This information is not available in the supplementary materials.Evaluating more models is a good thing, but one should make sure that they actually understand and evaluate them correctly. 

**Learning to Rank Method**: The paper introduces a listwise learning-to-rank method for all models and claims this as a contribution. However, have the authors evaluated this ranking loss against regression loss? In fact, findings from the 2011 Yahoo Learning to Rank Challenge indicate that learning to rank may not significantly outperform pointwise regression or classification losses. In some cases, regression loss could be more effective if specific label values are available. see [1] section 6.3. I do not think listNet is a powerful learning to rank algorithm. The author should report convincing results that  listNet is better than basic regression loss.

### Questions
no

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
While numerous datasets exist to evaluate model effectiveness in predicting protein structures, this paper highlights the need for datasets focused on assessing model performance in predicting proteins with specific functional capabilities. For example, can models predict functional variants of TadA, where certain high-efficiency variants demonstrate superior gene-editing capabilities compared to control counterparts. To address this, the authors introduce the dataset NovoBench 100K, which includes ~100 unique DNA variants, each experimentally derived by the authors in a wet lab and associated with a value indicating editing efficiency.

This dataset is divided to provide both in-domain and out-of-domain splits for training and testing. The authors then test 80 models spanning 24 papers on their effectiveness in ranking sequences based on ground truth efficiency scores. Experimental results reveal that BLMs perform well in in-domain ranking, However, BLMs show limited performance for out-of-domain ranking, underscoring a significant challenge in generalizing to unfamiliar data.

### Strengths
The paper introduces a dataset that addresses a crucial evaluation criterion (specific functional predictions) for model performance.

The paper evaluates over 80 models across 24 papers spanning protein, DNA, RNA, and multimodal domains which is an impressive and commendable effort, adding significant value to the study.

The paper includes a detailed comparison and analysis of BLMs, examining factors such as modality, model size, and K-mer.

### Weaknesses
Questions to improve clarity:

I think the the papers is a bit a hard to read and there are several open questions which could improve the clarity of the paper noted below -

(1) How is the read score representative of the evolution effectiveness? Is the least ranking sequence in the dataset completely ineffective at editing or all the 100K variants effective? Specifically I would like to know if you are also evaluating BLMs capability in predicting both effectiveness and ineffectiveness?  
(2) What external evaluation can you provide to show your effectiveness scores are sound and consistent with previous work / distaste ?
(3) Though Figure 4 is a helpful visualization, I think some kind of end to end pipeline of data construction and usage is helpful, currently the main framework is mixed up with the details provided. 
(4) Figure 5 shows range of metric value is between (0.82-0.86) for out-of-domain evaluation, the equivalent score range for in-domain evaluation is (0.85-0.92)? Do  you consider this a significant drop?  What is the drop per model, perhaps a scatter plot with x-axis as in-domain performance and y-axis as out of domain performance per model is helpful? Could other factors like  batch-effects etc be effecting the performance of out-of-domain generalization ?

Significance: 

Its unclear on how well evaluating on this task will generalize to other functional prediction tasks and what it the overall recommendation of the dataset for future evaluation. 

(1) Given that BLMs area able to achieve a given performance in predicting TadA evolution what other related function prediction tasks will this performance generalize to? And other tasks it wont?  What are the limtations of the datasets and What is the recommendation on how the dataset can be used by model developers?

### Questions
It would be helpful to receive a response from the authors on the questions described above.

### Soundness
3

### Presentation
2

### Contribution
2

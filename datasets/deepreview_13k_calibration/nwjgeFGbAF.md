# Better Call Graphs: A New Dataset of Function Call Graphs for Malware Classification

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 5, 3

## Abstract
Malware classification by using function call graphs (FCG) is an important task in cybersecurity.
One big challenge in this direction is the lack of representative, large, and unique FCG datasets.
Existing datasets typically contain obsolete Android application packages (APKs), largely consist of small graphs, and include many duplicate FCGs due to repackaging.
This results in misleading graph classification performance.
In this paper, we propose a new comprehensive dataset, Better Call Graphs (BCG), that contains large and unique FCGs from recent APKs, along with graph-level APK features, with benign and malware samples from different types and families.
We establish the necessity of BCG through the evaluation of several baseline approaches on existing datasets.  
BCG is available at https://iclr.me.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper creates a new dataset for malware. Current Android datasets are outdated and limited in size. Importantly, they often also have duplication, which can be harmful for research. For example, baseline tests on existing datasets highlighted how outdated samples can skew classifier performance. These researchers downloaded malware from AndroZoo and VirusShare, filtered them to find suitable current data, and then used various tools to categorize them.

### Strengths
This seems to be a sound way to filter APKs and featurizing them, especially combining graph-level features with the function call graph features. Definitely is a necessary advancement to research, as malware datasets are currently quite old.

### Weaknesses
It would be nice to have non-Android (x86) malware. 
identifying specific changes in APK structures over time: this is often an important part of malware research - how do these features and graph structures change over time? Similarly, how does this do on unseen data (new families that arise)? 
This dataset relies on existing tools like VirusTotal for malware classification and AVClass for label assignment. While I personally don't think this is necessarily an issue, I do think it's relatively a weakness in terms of novelty of methodology.

### Questions
Are GIN and GraphSage really the most advanced baselines you have? I think there are malware-specific works that could be useful to this discussion rather than relatively old graph baselines. 
What are the statistics on how the classifications/family distrubtions change over time.

### Soundness
4

### Presentation
4

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
The authors propose a dataset for function call graphs (FCGs) from
Android APKs in the task of malware classifcation.  They downloaded
more recent APKs, determined family and type, constructed FCGs, and
removed graphs with fewer than 100 edges and duplicates.  The
resulting dataset has 9938 graphs, with an average of 25k nodes and
54k edges. It contains 29 types and 118 families.

They extracted non-graph APK features (AF), such as servies,
receivers, and libraries.  They also extracted graph features (GF)
such as number of nodes/edges, largest connected component size, and
centrality metrics.  Finally, they extracted node representation based
on LDP (Cai and Wang, 2018) for some of their experiments.

They compare Random Forrest with different combination of features
with 3 GNN algorithms.  Empirical result indicate Random Forest using
all 3 types of features generally outperforms.

### Strengths
The authors propose a dataset for function call graphs (FCGs) from
Android APKs in the task of malware classifcation.  They downloaded
more recent APKs, determined family and type, constructed FCGs, and
removed graphs with fewer than 100 edges and duplicates.  The
resulting dataset has 9938 graphs, with an average of 25k nodes and
54k edges. It contains 29 types and 118 families.

They extracted non-graph APK features (AF), such as servies,
receivers, and libraries.  They also extracted graph features (GF)
such as number of nodes/edges, largest connected component size, and
centrality metrics.  Finally, they extracted node representation based
on LDP (Cai and Wang, 2018) for some of their experiments.

They compare Random Forrest with different combination of features
with 3 GNN algorithms.  Empirical result indicate Random Forrest using
all 3 types of features generally outperforms.

### Weaknesses
New algorithmic methods were not proposed and evaluated.

More non-graph features could have been extracted, such as n-grams of instructions.

### Questions
Why LDP was chosen to generate node embeddings?

The number of nodes across graphs is a variable, how are the node embeddings of a graph converted into a fixed-length feature vector for Random Forest?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a new comprehensive datasetthat contains large and unique FCGs from recent APKs, along with graph-level APK features.

### Strengths
1. A new dataset is proposed.
2. The paper is well organized.

### Weaknesses
The collection and construction of the dataset lack distinctiveness. The inclusion of new software and non-repetitive samples does not constitute the primary contribution of the paper.

I am not entirely sure why the authors refer to their dataset as the FCG dataset. Other FCG datasets mentioned by the authors, such as Drebin and CIC, provide SHA256 hashes or APK files, which are not directly related to FCG. Additionally, the Drebin dataset paper introduces a binary feature, not an FCG feature. Therefore, I am unsure why the authors classify their dataset as an FCG dataset.

The dataset relies heavily on VirusTotal's labeling. Although VirusTotal labeling remains the mainstream method, the authors mention, 'To ensure reliability, we only consider the APKs flagged by multiple antivirus engines in VirusTotal.' How many are considered 'multiple'? Which ones are they? Why were these specific ones chosen?

When labeling families using AVClass, there is significant noise. How should samples that cannot be consistently labeled with a family tag be handled?

The distribution of year categories is highly imbalanced. Why is this the case? It appears that the sample count is highest for the year 2021.

It is hoped that the authors can include the results of common detection methods for function call graph such as Mamadroid and APIGraph on BCG.

Similarly, when evaluating the detection performance for family classification, I anticipate the detection results of common malicious family classification methods (FalDroid [3] and MDMC [4]), rather than results based on common graph processing methods.

It is unclear whether the authors have provided temporal information for each APK. This would aid readers in conducting research on concept drift ([5]). Additionally, the authors could conduct additional experiments on concept drift, such as investigating how the model classification accuracy decreases with time on this dataset.

### Questions
1. I am not entirely sure why the authors refer to their dataset as the FCG dataset. Other FCG datasets mentioned by the authors, such as Drebin and CIC, provide SHA256 hashes or APK files, which are not directly related to FCG. Additionally, the Drebin dataset paper introduces a binary feature, not an FCG feature. Therefore, I am unsure why the authors classify their dataset as an FCG dataset.
2. The dataset relies heavily on VirusTotal's labeling. Although VirusTotal labeling remains the mainstream method, the authors mention, 'To ensure reliability, we only consider the APKs flagged by multiple antivirus engines in VirusTotal.' How many are considered 'multiple'? Which ones are they? Why were these specific ones chosen?
3. When labeling families using AVClass, there is significant noise. How should samples that cannot be consistently labeled with a family tag be handled?
4. The distribution of year categories is highly imbalanced. Why is this the case? It appears that the sample count is highest for the year 2021.
5. It is hoped that the authors can include the results of common detection methods for function call graph such as Mamadroid and APIGraph on BCG.

[1] Enhancing State-of-the-art Classifiers with API Semantics to Detect Evolved Android Malware
[2] MAMADROID: Detecting Android Malware by Building Markov Chains of Behavioral Models


6. Similarly, when evaluating the detection performance for family classification, I anticipate the detection results of common malicious family classification methods (FalDroid [3] and MDMC [4]), rather than results based on common graph processing methods.

[3] Android Malware Familial Classification and Representative Sample Selection via Frequent Subgraph Analysis
[4] Byte-level malware classification based on Markov images and deep learning.

7. It is unclear whether the authors have provided temporal information for each APK. This would aid readers in conducting research on concept drift ([5]). Additionally, the authors could conduct additional experiments on concept drift, such as investigating how the model classification accuracy decreases with time on this dataset.

[5]Transcending Transcend: Revisiting Malware Classification in the Presence of Concept Drift


Some related papers that I think need to be studied：
MalRadar: Demystifying Android Malware in the New Era

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new comprehensive dataset, Better Call Graphs (BCG), that contains large and unique FCGs from recent APKs,
along with graph-level APK features, with benign and malware samples from different types and families. The BCG datasets and existing datasets are evaluated on several baseline approaches to demonstrate the necessity of the BCG dataset.

### Strengths
This paper addresses the limitations of existing malware classification datasets, particularly the issue of outdated malware samples. A new, open-source dataset has been created, covering malware samples from 2017 to 2023.

### Weaknesses
First, the primary contribution of this work is the creation of a new dataset covering recent malware samples. However, I do not think this contribution meets the expectation of ICLR. The creation of a new dataset is largely engineering efforts and lacks sufficient scientific contribution.

Second, the evaluation shows that baseline methods perform poorly on this newly created dataset. I would appreciate the author to design a new model that can work well on the new dataset to enhance the scientific contribution.

Third, I find the poor performance of the baseline methods somewhat unclear. Could the authors clarify the experimental setup? Specifically, was the baseline trained on a portion of the new dataset (e.g., 70%) and then tested on the remaining samples?

Finally, the new dataset spans malware samples from 2017 to 2023, yet there are several other datasets that include samples up to 2021. Do the samples in your dataset overlap with those in existing datasets? If overlaps exist, would collecting malware samples only from 2021 to 2023 have been sufficient?

### Questions
1. Clarify the contribution of this work, especially scientific contribution. 
2. Explain the experimental setup: whether baseline models are trained on the new created dataset?
3. Clarify the overlap between the new created datasets and existing datasets (especially those includes samples up to 2021).

### Soundness
3

### Presentation
3

### Contribution
3

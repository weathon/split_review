# Search and Retrieval in Semantic-Structural Representations of Novel Malware

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 1, 3, 3

## Abstract
In this study we present a novel representation for binary programs, which captures semantic similarity and structural properties.  Our representation is composed in a bottom-up approach and enables new methods of analysis.  We show that we can perform search and retrieval of binary executable programs based on similarity of behavioral properties, with an adjustable level of feature resolution.  We begin by extracting data dependency graphs (DDG), which are representative of both program structure and operational semantics.  We then encode each program as a set of graph hashes representing isomorphic uniqueness, a method we have labeled DDG Fingerprinting.  Next, we use k-Nearest Neighbors to search in a metric space constructed from examples.  This approach allows us to perform a quantitative analysis of patterns of program operation. By evaluating similarity of behavior we are able to recognize patterns in novel malware with functionality not previously identified.  We present experimental results from search based on program semantics and structural properties in a dataset of binary executables with features extracted using our method of representation.  We show that the associated metric space allows an adjustable level of resolution.  Resolution of the features may be decreased for breadth of search and retrieval, or as the search space is reduced, the resolution may be increased for accuracy and fine-grained analysis of malware behavior.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author introduces a novel method for representing binary program features. This method utilizes data dependency to express the operational semantics and structural characteristics of the program, effectively capturing its semantic and functional aspects. Furthermore, the author introduces a bottom-up feature construction approach, enabling additional reasoning based on existing knowledge.

### Strengths
This article addresses a crucial field, considering the rapid proliferation of malware. Swift detection of zero-day malware and the identification of code reuse in zero-day malware present intriguing and formidable challenges. 

The article introduces the DDG Fingerprinting method for detecting malware similarity, significantly enhancing the interpretability of detection outcomes.

### Weaknesses
In the Data Collection section, why were those two categories chosen, and other categories not considered? Are the malicious categories up-to-date?

Important terms should be further clarified, such as the frequently references ``resolution''. I couldn't find a clear and detailed definition or explanation of this term.

How are the issues encountered in reverse engineering addressed, such as code obfuscation and anti-debugging techniques? I believe reverse engineering is not a trivial matter, yet it is only briefly discussed.

In the Data Dependency Graph Extraction section, it isclaimed to be an undirected graph, yet Figure 1 shows a directed graph. Moreover, there is no explanation about 'ai' in Figure 1. Why is the 'mov' instruction singled out as capturing most changes without any data or experimental support to back this claim?

Figure 5 lacks detailed information on the horizontal and vertical axes, making it difficult to understand. More detailed analysis would be better.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work presents an approach to generate malware representation using static analysis. That is, pieces of dependency graphs are built based on the assembly instructions of a given malware sample and then hashed using the Weisfeiler-Lehman graph hashing algorithm to retain the semantics of the dependency graphs and graph isomorphism. Finally, the hash values can be used to compute with Hamming Distance and KNN clustering. Only few evaluations with limited samples demonstrated the potential of the work.

### Strengths
- Clear presentation

### Weaknesses
The novelty of this method is limited, as it builds upon existing methods such as DDG, graph hash, and knn.
The experimental setup is overly simplistic, hindering the ability to effectively demonstrate the method's efficacy.

### Questions
Questions:
- Is it possible to show the semantic preserving when assembly codes were transformed into blocks of dependency graphs and hash values?

Suggestion:
- A clear contribution can be shown with comprehensive evaluations of large-scale samples and compared with other approaches, such as control-flow malware variant detection (Cesare et. al., 2013).

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author proposes a novel representation method for binary programs. First, reverse engineering is employed to extract data dependency graphs (DDGs) from each program. Subsequently, a set of graph hashes is utilized to represent the distinct basic block segments within a DDG. By comparing the DDG Fingerprint of an unknown program with existing programs, the author employs k-Nearest Neighbors to determine its functionality. This approach enables the identification of the functionality of unknown programs through the comparison of DDGs.

### Strengths
The topic of searching and retrieving novel malware is both intriguing and significant. 
The paper's structure and logic are lucid. 
The discovery of a similarity between ZeusGameover Feb2014 and the Client/Server Runtime Subsystem is interesting.

### Weaknesses
 **Missing a clear evaluation of the results.** The authors show one example retrieval, but all the discussion of Sect.3 is not enough to clarify the optimality and soundness of the proposal. In particular, how a practitioner could validate that the algorithm is picking up from the corpus of data meaningful neighbours? Also, the authors do no specify *why* the results of Fig.7 are relevant. What have these in common? The authors should provide some ground truth, trying to explain why they achieved those results. Otherwise, if the methods would have retrieved other 7 samples, what would have been the conclusion?

**Possible errors in disassembly.** The authors state that they leverage *objdump* as disassembler. However, there are plenty of techniques that malware programs use to avoid reverse engineering, such as packing, obfuscation, and anti-disassembly tricks. These techniques can lead to *objdump* producing incorrect or incomplete assembly code. Usually, practitioners leverage other tools like IDA and Ghidra that are better in disassembly than objdump, as they employ more sophisticated algorithms to handle these obfuscation techniques. Thus, the results might be biased towards the representation that is tool is providing, rather than capturing the intended functionality and graph shapes. The lack of a robust disassembly process undermines the reliability of the extracted Data Dependency Graphs (DDGs).

**Confused paper structure.** The manuscript would benefit for a re-arrangement of its structure. First, the abstract starts directly with the problem to solve, making it for newcomers to understand what is the problem to solve and why. Then, the introduction is missing which are the core contribution of the paper (hinted in Sect.2, but in a confused way). Most of the discussion is focused on just one cherry-picked example. There are no limitations, and no code is provided (that would have removed the need for Sect 4.1).

### Questions
1.The novelty of the proposed method is limited as it heavily relies on existing methods, thus the innovation of this paper is considered to be constrained.

2.The motivation behind selecting DDG as a feature is not adequately explained. Specifically, it is unclear what advantages this feature offers compared to other features such as control flow graphs or function call graphs in the context of software search and retrieval tasks.

3.The definition of Feature Resolution is excessively abstract, making it difficult to comprehend. It would be beneficial to provide an early explanation of this concept in the introduction section.

4.The DDG Fingerprint constructed by the authors appears to have a very high dimensionality, resulting in sparse data. Although the authors mention that “the feature resolution can be adjusted once the specific characteristics of the search have been refined”, I still struggle to understand how these specific characteristics are determined.

5.The experimental section is overly simplistic. 1), constructing a benign sample library with only 500 data is insufficient. 2), quantitative experiments are lacking. The authors only conducted qualitative analyses without providing accuracy metrics for identifying similarities between samples. 3), the use of only two selected samples in Figure 6 does not sufficiently establish the credibility of the results.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a methodology for retrieving malware from a large corpus of data through a kNN algorithm applied on a novel feature extraction set, leveraging on Data Dependancy Graphs (DDG). Each program of the corpus is then expressed as a set of hashes that describe them, and that they can be used to be retrieved at need.
The authors describe some cherry-picked results to clarify how their methodology work, also showing an example of the first 7 neighbours of the Sekoia Rootkit.

### Strengths
1. Interesting retrieval approach that could be used to understand similarities between malware.
2. The approach is easy to understand.

### Weaknesses
**Missing a clear evaluation of the results.** The authors show one example retrieval, but all the discussion of Sect.3 is not enough to clarify the optimality and soundness of the proposal. In particular, how a practitioner could validate that the algorithm is picking up from the corpus of data meaningful neighbours? Also, the authors do no specify *why* the results of Fig.7 are relevant. What have these in common? The authors should provide some ground truth, trying to explain why they achieved those results.
Otherwise, if the methods would have retrieved other 7 samples, what would have been the conclusion?

**Possible errors in disassembly.** The authors state that they leverage *objdump* as disassembler. However, there are plenty of techniques that malware programs use to avoid reverse engineering. Usually, practitioners leverage other tools like IDA and Ghidra that are better in disassembly than objdump. Thus, the results might be biased towards the representation that is tool is providing, rather than capturing the indended functionality and graph shapes.

**Confused paper structure.** The manuscript would benefit for a re-arrangement of its structure. First, the abstract starts directly with the problem to solve, making it for newcomers to understand what is the problem to solve and why. Then, the introduction is missing which are the core contribution of the paper (hinted in Sect.2, but in a confused way). Most of the discussion is focused on just one cherry-picked example. There are no limitations, and no code is provided (that would have removed the need for Sect 4.1).

### Questions
1. Which are the advantage of using this method, and not other retrieval methods? The paper states the presence of related work, but none is compared to the proposed technique.
2. How this technique can be validated?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

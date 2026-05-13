# Navigating Dataset Documentations in AI: A Large-Scale Analysis of Dataset Cards on HuggingFace

- Decision: Accept
- Scores: 8, 5, 8, 5

## Abstract
Advances in machine learning are closely tied to the creation of datasets. While data documentation is widely recognized as essential to the reliability, reproducibility, and transparency of ML, we lack a systematic empirical understanding of current dataset documentation practices. To shed light on this question, here we take Hugging Face -- one of the largest platforms for sharing and collaborating on ML models and datasets --  as a prominent case study. By analyzing all 7,433 dataset documentation on Hugging Face, our investigation provides an overview of the Hugging Face dataset ecosystem and insights into dataset documentation practices, yielding 5 main findings: (1) The dataset card completion rate shows marked heterogeneity correlated with dataset popularity: While 86.0\% of the top 100 downloaded dataset cards fill out all sections suggested by Hugging Face community, only 7.9\% of dataset cards with no downloads complete all these sections. (2) A granular examination of each section within the dataset card reveals that the practitioners seem to prioritize \textit{Dataset Description} and \textit{Dataset Structure} sections, accounting for 36.2\% and 33.6\% of the total card length, respectively, for the most downloaded datasets. In contrast, the \textit{Considerations for Using the Data} section receives the lowest proportion of content, accounting for just 2.1\% of the text. (3) By analyzing the subsections within each section and utilizing topic modeling to identify key topics, we uncover what is discussed in each section, and underscore significant themes encompassing both technical and social impacts, as well as limitations within the \textit{Considerations for Using the Data} section. (4) Our findings also highlight the need for improved accessibility and reproducibility of datasets in the \textit{Usage} sections. (5) In addition, our human annotation evaluation emphasizes the pivotal role of comprehensive dataset content in shaping individuals' perceptions of a dataset card's overall quality. Overall, our study offers a unique perspective on analyzing dataset documentation through large-scale data science analysis and underlines the need for more thorough dataset documentation in machine learning research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper performs an analysis of the quality of dataset cards, a form of data documentation, for 150 datasets on Hugging Face.

### Strengths
The motivation and context of the work are clearly explained. Dataset work is an important and undervalued aspect of machine learning research and this paper tackles an important topic given the prolifieration of ML datasets and platforms. The analysis and rationale are mostly presented clearly, such that it could easily be reproduced for another platform. The key insights are clearly highlighted, and they are interesting; the discussion of results is often insightful. The figures are beautiful and the captions well-done and self-contained (this is surprisingly rare, well done!). The discussion, limitations, and significance are well written. The metadata gathered (as far as I can tell) are formatted in a way that will enable future research in this direction.

### Weaknesses
Dataset curation, a very relevant domain, is not covered at all in related works. In general the related work lacks earlier works and perspective, e.g. from library science, which could have informed the analysis in the paper in some interesting ways. 
The human eval is not given much space compared to the other aspects and I think it could have provided a lot more insights.

### Questions
are the values given in the human eval averaged over the 5 annotators (each saw every dataset card?). If so, it would be interesting to see some inter-rater (dis)agreement, and some qualitative demonstration of e.g. which cards were high-agreement sort of gold standard, high agreement bad, and low agreement. 

What guidance were the raters given? What level of expertise did they have?

The correlation with content comprehensiveness in the human eval is not super high (~40%), and the rest are all quite low. It would be interesting to compare this with a qualitative description from the annotators of what they found made a better or worse card -- are there factors not detailed here they think it would be more informative to consider?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors conduct an analysis on a large array of Hugging face datasets, and their associated documentation. Their aim is to better understand what results in the popularity of a particular datasets, and perhaps standardize the documentation procedure of datasets

### Strengths
The paper is well written, easy to follow and digest. It is also interesting to study a large array of datasets.

### Weaknesses
- Most finding in the paper are “common sense” i.e. there always has been a high correlation with quality of documentation and usability of a particular tool/dataset
- It’s not clear how this paper fits ICLR conference, although it the study does conduct a comprehensive overview of the hugging face dataset cards and provides an insight on what makes the datasets popular they aren’t significantly new and their insight is limited
   - For example datasets may be simply popular because they are in a “hot” area of study
   - Another example is the quality of the underlying dataset – it may be the case the reason one of the datasets is very popular is simply attributed to the fact that there are many studies leveraging this dataset (which in some sense is correlated with the quality of the data)
- It seems a although there are several findings with respect to what makes a dataset popular, there isn’t a conclusive suggestion for improving dataset sharing/contribution.

### Questions
- The correlation between documentation length and popularity is not causal
   - I’d emphasize on the quality of the documentation and what points these “popular cards” address in the written documentation there may be a more granular set of points mentioned in each that results in their popularity
        - Data usability looks to have been a common key topic 
- It’s not clear how the power law with respect to data usage is useful
   - Power-law is quite pervasive -- for example in “popularity”
   - This power-law may simply represent the underlying distribution of people interested in deep learning topics/domains
      - E.g. text (NLP) versus mortgage tabular data (Finance)
- There’s a key component in the dataset documentation that is missing e.g. how the data is processed – perhaps this is covered in data usability?
   - By having a raw data card with associated derivatives simply being a modified transformation of the raw could drastically help with reproducibility
   - Further this way of representing allows for more comprehensive analysis on how various preprocessing steps effect benchmarks
       - these are much more important considerations in time-series, and healthcare domains for example.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper gives an analysis of dataset documentation practices by data creators. They focus on a Hugging Face’s data repository. The authors highlight findings such as frequently downloaded datasets are also often well documented, the fact that social concerns are some of the least documented and that users care about operational matters related to dataset - these may include, versioning, download details… etc. This work is a continuation of work championed by many ML researchers concerned with documentation and auditing to better understand ethical implications of our tools.

### Strengths
It is useful to provide these kinds of evaluations on new documentation processes. The ideas of how to document the different pieces of the ML process, though important, are still new and should change where there is a need. This type of study gives us a way to see where things are working and where improvements are needed. Eg. Inclusion of a uses section. Additionally, the authors started hinting on some of the relationships between what sections of the data card get filled in and the motivations of the data creators. Additionally,it is once again reminded  that we have to continue searching for better incentives to get dataset creators better document their datasets beyond describing what is in there. This work does not give us these answers and they are perhaps beyond the scope of this work but it is certainly another nudge that there is a lot more work here.

### Weaknesses
None for me. I think the paper did what it promised to do.

### Questions
- Were the authors able to find a correlation between well documented datasets and their creators? Eg, Do they come from other disciplines? Are they academic or industry researchers? Start-ups...etc
- Is there a relationship between the features included in the dataset and whether there is going to be a limitations section? ie do datasets that contain more sensitive data likely to be well documented and include limitations sections?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper conducts a large scale analysis on dataset cards from HuggingFace. The paper contributes mainly 5 findings which offers a unique perspective on dataset documentations.

### Strengths
1. The paper is well written with each finding clearly explained and backed by statistical data analysis
2. Through various data analysis, the paper showed quite a few insights on the current status of dataset cards, which are often under-studied from previous works.
3. The paper empirically verified the hypothesis proposed by employing human annotations. 
4. Through the study of HuggingFace dataset cards, the paper proposes new documentations practices that could be adopted by the industry to improve dataset documentations.

### Weaknesses
1. The paper only analyzes the documentations from HuggingFace, thus the potential for the findings to apply to other platforms remains unclear. Are there any suggestions from the authors on how to process dataset cards on other platforms?
2. The paper uses exact keyword matching to identify corresponding subsections. Thus it's hard to know the proportion of dataset cards which covers the corresponding subsection but with different keywords. 
3. Although the paper proposes new standard that the industry should follow, are there any methods the authors think that could help achieve this goal? 
4. How are the human annotators selected? Are they machine learning domain experts?

### Questions
See my questions in weakness section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

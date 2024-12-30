# On-prem-to-Cloud-Sale-Data-Automation

I recently completed a project where I automated a seamless data pipeline to refresh and update a Power BI dashboard every single day, ensuring that the latest data is always available for insights.

Breakdown of the pipeline:

1. 𝐀𝐳𝐮𝐫𝐞 𝐃𝐚𝐭𝐚 𝐅𝐚𝐜𝐭𝐨𝐫𝐲 – The pipeline begins by transferring data from an on-prem MySQL database to Azure Storage Account Gen2 (Silver layer).
2. 𝐃𝐚𝐭𝐚𝐛𝐫𝐢𝐜𝐤𝐬 𝐏𝐲𝐒𝐩𝐚𝐫𝐤 – The data undergoes transformation using PySpark in Databricks, i.e. modify date formats, adjust data types, and store it into the Azure Data Lake (Gold layer).
3. 𝐀𝐳𝐮𝐫𝐞 𝐒𝐲𝐧𝐚𝐩𝐬𝐞 𝐀𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬 – I use Synapse to create a pipeline that extracts metadata and iterates over stored procedures to generate views.
4. 𝐏𝐨𝐰𝐞𝐫 𝐁𝐈 𝐈𝐧𝐭𝐞𝐠𝐫𝐚𝐭𝐢𝐨𝐧 – Finally, the Power BI dashboard connects to Azure Synapse, presenting sales data by gender, product categories, and total sales, all with interactive slicers for a detailed analysis.

A fully automated system that updates sales insights daily.

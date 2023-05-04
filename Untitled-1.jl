# use the !kaggle datasets download -d azminetoushikwasi/cr7-cristiano-ronaldo-all-club-goals-stats to download the datasets

using Pkg 

# Pkg.add("CSV")
# Pkg.add("DataFrames")
# Pkg.add("StatsBase")
# Pkg.add("Plots")
using CSV
using DataFrames
using StatsBase
using Plots

df = DataFrame(CSV.File("./data.csv"))

df[!, :Competition] = replace.(df[!, :Competition], "Ã§" => "ç")
df[!, :Competition] = replace.(df[!, :Competition], "Italy Cup" => "Coppa Italia")
df[!, :Competition] = replace.(df[!, :Competition], "Liga Portugal" => "Primeira Liga")
df[!, :Competition] = replace.(df[!, :Competition], "Taça de Portugal Placard" => "Taça de Portugal")

FIXME:print(describe(df))


# cluster the goals based on the competition using StatsBase.jl 
# print(countmap(df[!, :Competition]))

# plot the competitions based on the goals scored

bar!(countmap(df[!, :Type]), legend = false, title = "Type_of_goal", fmt = :png,rotation=90)
savefig("type_of_goal.png")



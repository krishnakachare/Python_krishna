# // var
# a = 123;
#
# // (function(){
# // var b = 10
# // console.log(b)
#    //})()
#
# // IIFE
#
# // console.log(a) //
# // console.log(b) // undefined
#
# // if (true){
#
# // let a = 10;
# // console.log(a)
# //}
# // console.log(a) // reference
# error: undefined
#
# // if (true){
# // const b = 10
# //}
# // console.log(b)
#
# // Module
# design
# pattern
# // var
# flowers = () = > {
#
#                  // let
# rose = "green";
# // let
# lily = "white"
#
#        // const
# printColor = (color) = > {
#                          // console.log(color + rose)
#                          // console.log(color + lily)
#
#                          //}
# // const
# hello = () = > rose;
# // return {
#
#           // printColor,
# // hello
#
#    //}
#
# //}
# // const
# a = flowers()
#     // a.printColor("white")
#     // console.log(a.hello())
#
#     // function
# flower()
# {
# // let
# rose = "white"
# // let
# lily = "black"
#
# // this.printColor = (color) = > {
#                                  // console.log(color + rose)
#                                  // console.log(color + lily)
#
#                                  //}
# // this.hello = () = > rose;
# // return {
#           // hello,
# // printColor
#    //}
#
# //}
#
# // flower().hello() \
#    // flower().printColor("white")
#
#
# class Car {
#
# constructor(color, reg){
#
# this.color = color
# this.reg = reg
# }
#
# printColor(){
# console.log(this.color)
# }
#
# printreg(){
#
# console.log(this.reg)
# }
#
# Rcolor(){
#
#
# return this.color
# }
#
# Rreg()
# {
# return this.reg
# }
#
# }
#
#
# const
# abc = new
# Car("whirte", 99)
# abc.printColor()
#
# //
#
#
# class Car {
# // constructor(color, reg){
#
# // this.color = color;
# // this.reg = reg;
#
# // this.printColor = () = > {
# // console.log(this.color);
# //}
#
# // this.Rcolor = function(){
# //
#
#
# return this.color
# //}
#
# //}
#
# //}
#
# // const
# abc = new
# Car("whire", 99)
# // abc.printColor()
# // console.log(abc.Rcolor())
#
# //
#
#
# class hello{
#
#   # abc = 0
# //  # cde = "hello"
# // printAlpha(){
#
# // console.log(this.  # abc)
# // console.log(this.  # cde)
#
# //}
#
# //}
#
# // var a = hello()
# // a.printAlpha()
#
# // console.log(a.abc)
# // console.log(a.cde)
#
# // Map(), weakMap()
formatter = "%r %r %r %r";

print (formatter % (1,2,3,4));
print (formatter % ('Choco','Vanilla','Berries' ,'J' ) );
print (formatter % (
	"There was",
	"a Cookie box",
	"with a rare cookie",
	"guess which one"
) )

print (formatter %("_","_","_","-"))
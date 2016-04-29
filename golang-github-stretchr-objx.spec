Name     : golang-github-stretchr-objx
Version  : 0
Release  : 5
URL      : https://github.com/stretchr/objx/archive/cbeaeb16a013161a98496fad62933b1d21786672.tar.gz
Source0  : https://github.com/stretchr/objx/archive/cbeaeb16a013161a98496fad62933b1d21786672.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-github-stretchr-testify

%description
# objx
* Jump into the [API Documentation](http://godoc.org/github.com/stretchr/objx)

%prep
%setup -q -n objx-cbeaeb16a013161a98496fad62933b1d21786672

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/stretchr/objx
rm -rf %{buildroot}
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for file in $(find . -iname "*.go") ; do
     install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
     cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/stretchr/objx/accessors.go
/usr/lib/golang/src/github.com/stretchr/objx/accessors_test.go
/usr/lib/golang/src/github.com/stretchr/objx/constants.go
/usr/lib/golang/src/github.com/stretchr/objx/conversions.go
/usr/lib/golang/src/github.com/stretchr/objx/conversions_test.go
/usr/lib/golang/src/github.com/stretchr/objx/doc.go
/usr/lib/golang/src/github.com/stretchr/objx/fixture_test.go
/usr/lib/golang/src/github.com/stretchr/objx/map.go
/usr/lib/golang/src/github.com/stretchr/objx/map_for_test.go
/usr/lib/golang/src/github.com/stretchr/objx/map_test.go
/usr/lib/golang/src/github.com/stretchr/objx/mutations.go
/usr/lib/golang/src/github.com/stretchr/objx/mutations_test.go
/usr/lib/golang/src/github.com/stretchr/objx/security.go
/usr/lib/golang/src/github.com/stretchr/objx/security_test.go
/usr/lib/golang/src/github.com/stretchr/objx/simple_example_test.go
/usr/lib/golang/src/github.com/stretchr/objx/tests.go
/usr/lib/golang/src/github.com/stretchr/objx/tests_test.go
/usr/lib/golang/src/github.com/stretchr/objx/type_specific_codegen.go
/usr/lib/golang/src/github.com/stretchr/objx/type_specific_codegen_test.go
/usr/lib/golang/src/github.com/stretchr/objx/value.go
/usr/lib/golang/src/github.com/stretchr/objx/value_test.go

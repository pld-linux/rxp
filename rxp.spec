Summary:	XML 1.0 validating parser
Summary(pl):	XML 1.0 validating parser
Name:		rxp
Version:	1.3.0
Release:	1
License:	GPL
Group:		Applications/Publishing/XML
Source0:	ftp://ftp.cogsci.ed.ac.uk/pub/richard/%{name}-%{version}.tar.gz
# Source0-md5:	c894ea89b22ce398a830d8d6bf650fc8
#Patch0:		%{name}-xmlcache.patch
URL:		http://www.cogsci.ed.ac.uk/~richard/rxp.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RXP is a validating XML parser written in C.

%description -l pl
RXP to waliduj±cy parser XML napisany w jêzyku C.

%prep
%setup -q
#%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags} -DCHAR_SIZE=16"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install rxp $RPM_BUILD_ROOT%{_bindir}
install rxp.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
